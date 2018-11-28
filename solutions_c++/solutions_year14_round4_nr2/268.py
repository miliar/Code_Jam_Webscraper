#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

#define INF 2000000000

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

const int MAXN = 100100;
int a[MAXN];

void solve(int test) {
	int n;
	scanf("%d", &n);
	map<int, int> pos;
	forn(i, n) {
		scanf("%d", a + i);
		pos[a[i]] = i;
	}
	int fpos = 0, lpos = n - 1;
	ll ans = 0;
	for (map<int, int>::iterator it = pos.begin(); it != pos.end(); ++it) {
		int num = it->first;
		int cpos = it->second;
		if (cpos - fpos < lpos - cpos) {
			ans += cpos - fpos;
			for (int i = cpos; i > fpos; --i) {
				a[i] = a[i - 1];
				pos[a[i]] = i;
			}
			a[fpos] = num;
			++fpos;
		} else {
			ans += lpos - cpos;
			for (int i = cpos; i < lpos; ++i) {
				a[i] = a[i + 1];
				pos[a[i]] = i;
			}
			a[lpos] = num;
			--lpos;
		}
	}
	cout << ans << endl;
}

int main(int argc, char **argv) {
//	freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tt;
	scanf("%d\n", &tt);
	forn(i, tt) {
		printf("Case #%d: ", i + 1);
		solve(i + 1);
	}
	return 0;
}
