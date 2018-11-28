#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

string tostring(int n, int len){
  bitset<64> bs = n;
  string s = bs.to_string().substr(64 - len);
  return s;
}

bool f(int n, long long b, long long m, int len){
  long long ret = 0;
  long long t = 1;
  for(int i = 0; i < len; ++i){
    int bit = (n >> i) & 1;
    ret = ret + t * bit;
    ret = ret % m;
    t = (t * b) % m;
  }

  return (ret == 0);
}

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    cout << "Case #" << ncase << ": " << endl;

    int len, total;
    cin >> len >> total;

    long long limit = 1LL << (len - 2);
    for(int mask = 0; mask < limit; ++mask){
      long long n = 1LL << (len - 1);
      n |= mask << 1;
      n |= 1;

      bool good = true;
      vector<int> ans(11, 0);

      for(int b = 2; b <= 10; ++b){
        for(int m = 2; m < 1000; ++m){
          if(f(n, b, m, len)){
            ans[b] = m;
            break;
          }
        }
        if(ans[b] == 0){
          good = false;
          break;
        }
      }

      if(good){
        cout << tostring(n, len);
        for(int b = 2; b <= 10; ++b){
          cout << " " << ans[b];
        }
        cout << endl;
        total--;
      }

      if(total == 0){
        break;
      }
    }
  }

  return 0;
}
