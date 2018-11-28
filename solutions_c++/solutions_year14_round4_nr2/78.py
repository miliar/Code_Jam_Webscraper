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

int T, n, a[11000], b[11000];
bool cmp(int x, int y)
{
	return a[x] < a[y];
}
int main()
{
	int ca = 0;
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int r = 0;
			for (int j = 0; j < n - i; j++)
				if (a[j] < a[r])
					r = j;
			if (r <= n - i - 1 - r) {
				ans += r;
			} else {
				ans += n - i - 1 - r;
			}
			for (int j = r; j < n - i - 1; j++)
				swap(a[j], a[j + 1]);
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
}
