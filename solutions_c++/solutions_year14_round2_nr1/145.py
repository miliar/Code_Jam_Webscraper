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

using namespace std;
char s[105][105];
char tmp[105], pt[105];
vector<int> v[105];
int main() {
	int i, j, k, n, l;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		for (i = 0; i < n; ++i) {
			scanf("%s", s[i]);
		}
		l = 0;
		for (j = 0; s[0][j]; ++j) {
			if (j == 0 || s[0][j] != s[0][j - 1])
				tmp[l++] = s[0][j];
		}
		tmp[l] = 0;
		for (i = 0; i < l; ++i)
			v[i].clear();
		strcpy(pt, tmp);
		bool ok = true;
		for (i = 0; i < n; ++i) {
			k = 0;
			for (j = 0; s[i][j]; ++j) {
				if (j == 0 || s[i][j] != s[i][j - 1])
					tmp[k++] = s[i][j];
			}
			tmp[k] = 0;
			if (strcmp(tmp, pt) != 0)
				ok = false;
			k = 0;
			int c;
			for (j = 0; s[i][j]; ++j) {
				if (j == 0 || s[i][j] != s[i][j - 1]) {
					if (j)
						v[k - 1].push_back(c);
					tmp[k++] = j;
					c = 1;
				} else
					c++;
			}
			v[k - 1].push_back(c);
		}
		if (ok == false) {
			printf("Case #%d: Fegla Won\n", cas);
			continue;
		}
		int ans = 0;
		for (i = 0; i < l; ++i) {
			int mn;
			for (k = 1; k <= 100; ++k) {
				int p = 0;
				for (j = 0; j < v[i].size(); ++j) {
					p += abs(v[i][j] - k);
				}
				if (k == 1)
					mn = p;
				else
					mn = min(mn, p);
			}
			ans += mn;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
