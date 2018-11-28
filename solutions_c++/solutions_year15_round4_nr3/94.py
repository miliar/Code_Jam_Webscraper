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

const int INF = 100500;
const int MAXLEN = 1e6 + 10;
const int MAXN = 25;

int n;
map<string, int> num;
int sz;

vector<int> x[MAXN];

bool used[2][MAXLEN];

char s[MAXLEN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d ", &T);
	forn(test, T) {
		printf("Case #%d: ", test + 1);

		num.clear();
		sz = 0;

		scanf("%d ", &n);

		forn(i, n)
			x[i].clear();

		forn(i, n) {
			gets(s);
			int k = strlen(s);
			s[k++] = ' ';
			string t = "";
			forn(j, k)
				if (s[j] == ' ') {
					if (t != ".") {
						if (!num.count(t))
							num[t] = sz++;
						x[i].push_back(num[t]);
						t = "";
					}
				} else
					t += s[j];
		}

		int ans = INF;

		forab(mask, 1 << (n - 2), 1 << (n - 1)) {
			memset(used[0], 0, sizeof(int) * sz);
			memset(used[1], 0, sizeof(int) * sz);

			forn(i, n) {
				int q = ((mask >> (n - 1 - i)) & 1);
				forn(j, x[i].size())
					used[q][x[i][j]] = true;
			}

			int cnt = 0;

			forn(i, sz)
				if (used[0][i] && used[1][i])
					cnt++;

			ans = min(ans, cnt);
		}

		printf("%d\n", ans);

	}
	return 0;
}
