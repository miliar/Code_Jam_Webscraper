#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int ans = 11;
int X, N, f[10000];

int main()
{
  int T;
  cin >> T;
  for(int case_num = 1; case_num <= T; ++case_num) {
	cin >> N >> X;

	for(int i = 0; i < N; ++i) cin >> f[i];

    std::sort(&f[0], &f[N]);

    int ans = 0;
    for(int i = N - 1; i >= 0; --i) {
	  if(f[i] == -1) continue;
      for(int j = i - 1; j >= 0; --j) {
	    if(f[j] == -1) continue;
	    if(f[i] + f[j] <= X) {
		  f[j] = -1;
		  break;
		}
	  }
	  ++ans;
	}

	cout << "Case #" << case_num << ": " << ans << endl;
  }
  return 0;
}

