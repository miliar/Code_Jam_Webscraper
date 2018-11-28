// ================================================================================================
//  Written by Luis Garcia, 2014
// ================================================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ14_05A, "GCJ14 05A")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

int main(
	) {
		int T, N, X;
		cin >> T;

		for (int _T = 1; _T <= T; ++_T) {
			cin >> N >> X;

			vector<int> files;
			for (int i = 0, x; i < N; ++i) {
				cin >> x;
				files.push_back(x);
			}

			sort(files.begin(), files.end());

			int ans = 0;
			for (int i = 0, j = N - 1; i <= j;) {
				if (i == j)
					++ans, ++i, --j;
				else if (files[i] + files[j] <= X)
					++ans, ++i, --j;
				else
					++ans, --j;
			}

			cout << "Case #" << _T << ": " << ans << endl;
		}

		return 0;
	}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
