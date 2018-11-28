#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;
typedef long long LL;
vector <LL> p;

void getprime(){
  for (int i = 2; i <= 1e5; i++){
    bool ret = true;
    for (int j = 0; j < p.size(); j++){
      if (p[j] * p[j] > i) break;
      if (i % p[j] == 0){
        ret = false;
        break;
      }
    }
    if (ret) p.push_back(i);
  }
}

int checkprice(LL n){
  for (int i = 0; i < p.size(); i++){
    if (n % p[i] == 0) return p[i];
    if (p[i] * p[i] > n) break;
  }
  return 0;
}

void brute(int n, int m){
  if (m == 0) return;
  for (LL mask = (1ll << (n - 1)) + 1; mask < (1ll << n); mask += 2){
    vector <int> ans;
    bool isprime = false;
    for (int b = 2; b <= 10; b++){
      LL ret = 0, e = 1;
      for (int i = 0; i < n; i++){
        if ((mask>>i)&1) ret += e;
        e *= b;
      }
      LL tmp = checkprice(ret);
      ans.push_back(tmp);
      if (tmp == 0) isprime = true;
    }
    if (!isprime){
      string tmp;
      for (int i = n-1; i >= 0; i--){
        if ((mask>>i)&1) tmp+='1'; else tmp+='0';
      } 
      cout << tmp;
      for (int i = 0; i < 9; i++) cout << ' ' << ans[i];
      cout << endl;
      m--;
      if (m == 0) return;
    }
  }
}

void construct(int n, int m){
  if (m == 0) return;
  for (LL mask = (1ll << (n-2)); mask < (1ll << (n-1)); mask++){
      string tmp;
      for (int i = n-2; i >= 0; i--){
        if ((mask>>i)&1) tmp+='1'; else tmp+='0';
      }
      tmp += '0';
      cout << tmp;
      for (int i = 2; i <= 10; i++) cout << ' ' << i;
      cout << endl;
      m--;
      if (m == 0) return;
  }
}

int main(){
  getprime();
  int t; cin >> t;
  for (int cas = 1; cas <= t; cas++){
    int n, m; cin >> n >> m;
    cout << "Case #" << cas << ":" << endl;
    brute(n, m);
    //else construct(n, m);
  } 
  return 0;
}
