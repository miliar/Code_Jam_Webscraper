#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

int arr[110][110];
int row[110], col[110];

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif

	int T, n, m;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> n >> m;
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &arr[i][j]);
				row[i] = max(row[i], arr[i][j]);
				col[j] = max(col[j], arr[i][j]);
			}
		}
		bool flag = true;
		for (int i = 0; i < n && flag; ++i) {
			for (int j = 0; j < m && flag; ++j) {
				if (arr[i][j] < row[i] && arr[i][j] < col[j])
					flag = false;
			}
		}
		if (flag)
			printf("Case #%d: YES\n", t + 1);
		else
			printf("Case #%d: NO\n", t + 1);

	}
	return 0;
}
