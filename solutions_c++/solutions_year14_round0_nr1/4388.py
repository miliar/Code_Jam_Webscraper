#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <stdio.h>
typedef long long ll;
#define mset(a, val) memset(a, val, sizeof(a))
#define up(i, s, t) for (ll i = (s); i < (t); i += 1)
#define down(i, s, t) for (ll i = (s); i > (t); i -= 1)
#define rd1(a) scanf("%d", &a)
#define rd2(a, b) scanf("%d %d", &a, &b)
#define rd3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define rd4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define pii pair<int, int>

using namespace std;
const int MAXINT = 0x6fffffff;
const ll MAXLONG = (ll) 1 << 63 - 1;
const int MAXN = 4;

int arr[MAXN][MAXN];
int n;
set<int> se;

int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

	int t;
	cin >> t;
	up(ca, 1, t + 1) {
		se.clear();
		int a, b;
		rd1(a);
		a --;
		up(i, 0, 4) {
			up(j, 0, 4) {
				rd1(arr[i][j]);
			}
		}

		up(i, 0, 4) {
			se.insert(arr[a][i]);
		}

		rd1(b);
		b --;
		up(i, 0, 4) {
			up(j, 0, 4) {
				rd1(arr[i][j]);
			}
		}

		int cnt = 0;
		int res = -1;
		up(i, 0, 4) {
			if (se.find(arr[b][i]) != se.end()) {
				cnt ++;
				res = arr[b][i];
			}
		}

		printf("Case #%d: ", ca);
		if (cnt == 1) {
			printf("%d\n", res);
		} else if (cnt > 1) {
			puts("Bad magician!");
		} else {
			puts("Volunteer cheated!");
		}
	}
    return 0;
}