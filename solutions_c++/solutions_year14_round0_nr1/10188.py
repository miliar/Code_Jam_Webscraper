#include <iostream>
#include <algorithm>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdlib> 
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;
using namespace __gnu_cxx;

#define sz(x) (int)x.size()
#define round(x) (int)(x + 0.5)
#define pb(x) push_back(x)
#define all(x) (x).begin(), (x).end()
#define ins insert
#define getmax(a,b) ((a) > (b) ? (a) : (b))
#define getmin(a,b) ((a) > (b) ? (b) : (a))
#define mms(x,n,s) memset(x, n, sizeof(x) * s)
#define CV(x,n) count(all(x),(n))
#define FOR(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define rep(i, x, n) for (int (i) = (x); (i) < (n); (i)++)

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pair<int, int> > vpii;
typedef set<int> si;

int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};
int d8i [] = {0, 0, 1, -1, 1, 1, -1, -1};
int d8j [] = {1, -1, 0, 0, 1, -1, 1, -1};

    /*     		 \\^//           /*
    | |    Magic Starts Here     | |
    */     		 // \\           * /


int arr[5][5];
vi row(5);
vi row2(5);

int main() {
	#ifndef ONLINE_JUDGE
		freopen("A-small-attempt4.in", "rt", stdin);
		freopen("out.txt", "wt", stdout);
	#endif

	std::ios_base::sync_with_stdio(false);

	int t;
	int x, y;
	cin >> t;

	FOR(k, t) {
		cin >> x;
		FOR(i, 4) {
			FOR(j, 4) {
				cin >> arr[i][j];
			}
		}
		FOR(m, 4)
			row[m] = arr[x - 1][m];

		cin >> y;
		FOR(i, 4) {
			FOR(j, 4) {
				cin >> arr[i][j];
			}
		}
		FOR(m, 4)
			row2[m] = arr[y - 1][m];
		
		int res = 0;
		int ans;
		FOR(f, 4) {
			if (find(row.begin(), row.end(), row2[f]) != row.end()) {
				res++;
				ans = row2[f];
			}
		}

		if (res == 1) {
			cout << "Case #" << k + 1 << ": " << ans << endl;
		} else if (res > 1) {
			cout << "Case #" << k + 1 << ": " << "Bad magician!" << endl;
		} else if (res == 0) {
			cout << "Case #" << k + 1 << ": " << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}