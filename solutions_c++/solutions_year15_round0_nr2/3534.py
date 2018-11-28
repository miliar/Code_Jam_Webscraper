/* [themighty] deathsurgeon (Rupesh Maity)
* 2nd year, B.Tech in IT
* IIIT - Allahabad
*/

#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <stack>
#include <queue>
#include <vector>
#include <map>

using namespace std;

typedef long long LL;
typedef unsigned uint;
typedef pair<int, int> pii;

#define MOD 1000000007
#define MAX 1000000
#define pb push_back
#define yes puts("YES")
#define no puts("NO")
#define sd(x) scanf("%d", &x)
#define PI 3.14159265

int main() {
//	freopen("2input.txt", "r", stdin);
//	freopen("2output.txt", "w", stdout);

	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		int n;
		cin >> n;

		int cnt[2002] = { 0 };
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			++cnt[a];
		}

		int mn = 1000;

		for (int i = 999; i > 0; i--) {
			cnt[i] += cnt[i + 1];

			int p = i;
			int last = i + 1;
			int j = 1;
			while (last < 1001) {
				p += j*(cnt[last] - cnt[last + i]);
				last += i;
				++j;
			}

			if (p < mn)
				mn = p;
		}

		printf("Case #%d: %d\n", cas, mn);
	}

	return 0;
}
