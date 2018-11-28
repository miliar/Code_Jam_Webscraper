#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
int n;
vector <int> arr;

int main(){
  int t;
  cin >> t;
  for (int idx = 1; idx <= t; idx++){
    cout << "Case #" << idx << ": ";
    cin >> n; arr.resize(n);
    int hi = 0;
    for (int i = 0; i < n; i++){
      cin >> arr[i];
      hi = max(hi, arr[i]);
    }
    if (hi <= 3) {
      cout << hi << endl;
      continue;
    }
    int lo = hi;
    for (int num = 2; num <= hi; num++){
      int spec = 0;
      for (int i = 0; i < n; i++){
	if (arr[i] <= num) continue;
	int units = (arr[i] + num - 1) / num;
	spec += (units - 1);
      }
      lo = min(lo, num + spec);
    }
    cout << lo << endl;
  }
  return 0;
}
