#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int T;
int main(void){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int sm;
    string s;
    int c = 0;
    int ans = 0;
    cin >> sm >> s;
    for(int i = 0; i <= sm; i++){
      if(c < i){
	c++;
	ans++;
      }
      c += s[i]-'0';
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
}
