#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = acos(-1.);
const double eps = 1e-6;

int T, n, m, a1, s[1100];
int main()
{
	int ca = 0;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	for (scanf("%d", &T); T; T--) {
		scanf("%d%d", &n, &m);
		memset(s, 0, sizeof s);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a1);
			s[a1]++;
		}
		int ans = 0;
		for (int j = m; j > 0; j--) {
			while (s[j]) {
				s[j]--;
				ans++;
				for (int last = j; last > 0; last--) {
					if (s[last] && last + j <= m) {
						s[last]--;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
}
