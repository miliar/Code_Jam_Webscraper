#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;
int main(){
  int T; cin >> T;
  int idx =0;
  while(T--){
    ++idx;
    int n; cin >> n;
    string str; cin >> str;
    int current = str[0]-'0';
    int ans = 0;
    for(int i=1;i<=n;++i){
      if(current < i) {
	      ans += i-current;
	      current += i-current;
      }
      current += str[i]-'0';
    }
    cout <<  "Case #" << idx<<": "<<ans << endl;
  }
  return 0;
}
