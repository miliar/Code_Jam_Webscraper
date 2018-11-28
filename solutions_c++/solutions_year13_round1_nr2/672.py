#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

string fileName = "B-small-attempt0";

int a[10000];

void solveSingle(int testNumber) {
	int e, r, n;
	cin >> e >> r >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	int dp[20][20];
	memset(dp, -1, sizeof(dp));

	dp[0][e] = 0;

	for (int i = 0; i < n; i++)
		for (int j = 0; j <= e; j++) {
			if (dp[i][j] == -1) continue;
			for (int k = 0; k <= j; k++) {
				int t = min(e, j - k + r);
				dp[i + 1][t] = max(dp[i + 1][t], dp[i][j] + a[i] * k);
			}
		}
	int res = 0;
	for (int i = 0; i <= e; i++)
		res = max(res, dp[n][i]);
	printf("Case #%d: %d\n", testNumber, res);
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
		fflush(stdout);
	}
	return 0;
}
