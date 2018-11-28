#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef map<int, int> mii;

int T;
int X, R, C;

void solve()
{
	bool ansExist = false;
	if (X == 1) {
		ansExist = true;
	} else if (X == 2) {
		bool a[4][4] = {
			false, true, false, true,
			true, true, true, true,
			false, true, false, true,
			true, true, true, true
		};
		ansExist = a[R-1][C-1];
	} else if (X == 3) {
		bool a[4][4] = {
			false, false, false, false,
			false, false, true, false,
			false, true, true, true,
			false, false, true, false
		};
		ansExist = a[R-1][C-1];
	} else if (X == 4) {
		bool a[4][4] = {
			false, false, false, false,
			false, false, false, false,
			false, false, false, true,
			false, false, true, true
		};
		ansExist = a[R-1][C-1];
	}

	if (ansExist == true) {
		printf("GABRIEL");
	} else {
		printf("RICHARD");
	}

	return;
}

int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d", &X, &R, &C);
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}
