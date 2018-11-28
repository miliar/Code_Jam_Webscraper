#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 21;
const int MAXP = 1e4 + 10;

int p;
int e[MAXP];
int f[MAXP];

int a[MAXN];
int s[1 << MAXN];

map<int, int> to;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d ", &T);
	forn(test, T) {
		printf("Case #%d: ", test + 1);

		to.clear();

		scanf("%d", &p);
		forn(i, p) {
			scanf("%d", &e[i]);
			to[e[i]] = i;
		}
		forn(i, p)
			scanf("%d", &f[i]);

		int n = 0;
		s[0] = 0;

		assert(e[0] == 0);
		f[0]--;

		forn(i, p)
			while (f[i] > 0) {
				a[n] = e[i];
				forn(j, (1 << n)) {
					s[(1 << n) + j] = s[j] + a[n];
					f[to[s[j] + a[n]]]--;
				}
				n++;
			}

		forn(i, n)
			printf("%d%c", a[i], (i == n - 1 ? '\n' : ' '));

	}
	return 0;
}
