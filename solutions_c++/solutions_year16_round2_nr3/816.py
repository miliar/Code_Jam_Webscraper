
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXN 1010
#define MAXV 16
//-----------------------------------------------------------
int N;
char s[MAXN][2][22];
int ans[10];


int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%s%s", s[i][0], s[i][1]);
//			printf("%s  %s\n", s[i][0], s[i][1]);
		}

		int ans = 0;
		int tmp = 0;
		bool match[2];
		for (int i = 0; i < (1 << N); i++) {
			tmp = 0;
			for (int j = 0; j < N; j++) {
				// True one
				if (i & (1 << j)) continue;
				// Test
				match[0] = false;
				match[1] = false;
				for (int k = 0; k < N; k++) {
					if (i & (1 << k)) {
						if (!strcmp(s[j][0], s[k][0])) {
							match[0] = true;
						}
						if (!strcmp(s[j][1], s[k][1])) {
							match[1] = true;
						}
					}
				}
				if (match[0] && match[1]) {
					tmp++;
				}
			}
			ans = max(tmp, ans);
		}

		printf("Case #%d: %d", casenum++, ans);
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

