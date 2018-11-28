#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define BIG 1000000000
#define LL long long
#define MAXN 1010
using namespace std;

int ntest;
int n;
double a[MAXN], b[MAXN];
int f[MAXN][MAXN];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 1; test <= ntest; test++) {
		memset(f, 0, sizeof(f));
		cin >> n;
		for (int i = 1; i <= n; i++) cin >> a[i];
		for (int i = 1; i <= n; i++) cin >> b[i];
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		//for (int i = 1; i <= n; i++) cout << a[i] << ' '; cout << endl;
		//for (int i = 1; i <= n; i++) cout << b[i] << ' '; cout << endl;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				f[i][j] = max(f[i - 1][j], f[i][j - 1]);
				if (a[i] > b[j]) f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1);
			}
		int ans1 = f[n][n];
		int ans2 = n;
		int cur = 0;
		for (int i = 1; i <= n; i++) {
			bool found = false;
			for (int j = cur; j <= n; j++)
				if (b[j] > a[i]) {
					found = true;
					cur = j + 1;
					break;
				}
			if (found) ans2--;
			else break;
		}
		printf("Case #%d: %d %d\n", test, ans1, ans2);
	}
}

