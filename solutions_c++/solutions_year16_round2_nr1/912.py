
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
#define MAXN 2010
//-----------------------------------------------------------
int N;
int ord[10] = {0, 2, 8, 4, 6, 5, 7, 1, 3, 9};
int len[10] = {4, 3, 3, 5, 4, 4, 3, 5, 5, 4};
char d[10][6] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char s[MAXN];
int ans[10];

void solve() {
	bool find[5];
	int findcnt;
	for (int i = 0; i < 10; i++) {
		int v = ord[i];
		while(true) {
			findcnt = 0;
			memset(find, false, sizeof(find));
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < len[v]; k++) {
					if (find[k]) continue;
					if (s[j] == d[v][k]) {
						find[k] = true;
						findcnt++;
						break;
					}
				}
				if (findcnt == len[v]) break;
			}
			// find!
			if (findcnt == len[v]) {
				ans[v]++;
				findcnt = 0;
				memset(find, false, sizeof(find));
				for (int j = 0; j < N; j++) {
					for (int k = 0; k < len[v]; k++) {
						if (find[k]) continue;
						if (s[j] == d[v][k]) {
							s[j] = '0';
							find[k] = true;
							findcnt++;
							break;
						}
					}
					if (findcnt == len[v]) break;
				}
			} else {
				break;
			}
		}
	}
	for (int j = 0; j < N; j++) {
		if (s[j] != '0') {
			printf("fail!!\n");
			break;
		}

	}
}

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		scanf("%s", s);
		N = strlen(s);
		memset(ans, 0, sizeof(ans));
		solve();

		printf("Case #%d: ", casenum++);
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < ans[i]; j++) {
				printf("%d", i);
			}
		}
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

