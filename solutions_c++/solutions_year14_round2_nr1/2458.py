#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897932384626433832795
using namespace std;


int main() {
	int t, tc = 1, ans = 0;
	int n, i, l, idx, m, c[101][101], mid, k, tmp1[101];
	bool turn; string a; vector <int> b, tmp;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		turn = true; b.clear(); ans = 0;
		memset(c, 0, sizeof(c));
		scanf("%d", &n);
		cin >> a; m = a.size(); b.pb(a[0]); c[0][0] = 1;
		for(i = 1; i < m; i++) {
			if(a[i] != a[i - 1]) b.pb(a[i]);
			c[0][b.size() - 1]++;
		} k = b.size();
		for(i = 1; i < n; i++) {
			cin >> a;
			if(turn) {
				m = a.size(); tmp.clear();
				fill(tmp1, tmp1 + m + 1, 0);
				tmp.pb(a[0]); c[i][0] = 1;
				for(l = 1; l < m; l++) {
					if(a[l] != a[l - 1]) tmp.pb(a[l]);
					c[i][tmp.size() - 1]++;
				}
				if(tmp != b) turn = false;
			}
		}
		printf("Case #%d: ", tc++);
		if(turn) {
			for(i = 0; i < k; i++) {
				mid = c[0][i];
				for(l = 1; l < n; l++) mid = (mid + c[l][i]) >> 1;
				for(l = 0; l < n; l++) ans += abs(c[l][i] - mid);
			}
			printf("%d\n", ans);
		}
		else printf("Fegla Won\n");
	}
	return 0;
}
