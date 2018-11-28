#include <iostream>
#include <cstring>

using namespace std;

int heights[2501];

int main()
{
  int n, tc, tmp;
  cin >> tc;

  for(int i = 1; i <= tc; i += 1) {
    cin >> n;
    memset(heights, 0, sizeof(heights));
    
    for(int j = 0; j < n*2-1; j += 1) {
      for(int k = 0; k < n; k += 1) {
	cin >> tmp;
	heights[tmp] += 1;
      }
    }

    cout << "Case #" << i << ": ";
    tmp = 0;
    for(int j = 1; j < 2501; j += 1) {
      if(heights[j] % 2 != 0) {
	tmp += 1;

	if(tmp < n) {
	  cout << j << " ";
	} else {
	  cout << j << endl;
	  break;
	}
      }
    }
  }

  return 0;
}
