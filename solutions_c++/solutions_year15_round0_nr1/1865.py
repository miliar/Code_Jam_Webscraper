#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int t;
  cin >> t;
  for (int idx = 1; idx <= t; idx++){
    int n;
    cin >> n;
    string str; cin >> str;
    int res = 0;
    int ppl = 0;
    for (int i = 0; i <= n; i++){
      int num = (int) str[i] - '0';
      for (int j = 0; j < num; j++){
	if (ppl >= i) ppl++;
	else {
	  res += (i - ppl);
	  ppl += (i - ppl);
	  ppl++;
	}
      }
    }
    cout << "Case #" << idx << ": ";
    cout << res << endl;
  }

  return 0;
}
