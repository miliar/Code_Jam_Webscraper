#include <iostream>
#include <string>
using namespace std;
int main(){
  int t;
  cin >> t;
  for (int casecnt = 1; casecnt <= t; ++ casecnt){
    cout << "Case #" << casecnt << ": ";
    int smax;
    string str;
    cin >> smax >> str;
    int ans = 0;
    int cum = 0;
    for (int i = 0; i <= smax; ++ i){
      int curr = ((int)str[i])-48;
      if (cum < i) {
	ans += i-cum;
	cum = i;
      }
      cum += curr;
    }
    cout << ans << endl;
  }

}
