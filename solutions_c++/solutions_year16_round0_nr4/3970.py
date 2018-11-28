#include<iostream>
#include<algorithm>

using namespace std;
typedef long long Int;


void solve(){
  Int k , c, s;
  cin >> k >> c >> s;
  if(s * c < k){
    cout << "IMPOSSIBLE";
    return;
  }
  int p = 0;
  for(int i = 0;i < s;i++){
    Int res = 0;
    for(int j = 0;j < c;j++){
      res *= k;
      if(p < k)
	res += p++;
    }
    if(i)cout << " ";
    cout << res+1;
    if(p >= k)break;
  }
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}

