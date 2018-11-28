#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
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
#define MAXN 210
//-----------------------------------------------------------
ull N;
char s[MAXN];
char t[MAXN];
int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		memset(s, 0, sizeof(s));
		scanf("%s", s);
		int last = strlen(s) - 1;
		int first;
		int ans = 0;
		//printf("%s\n", s);
		while (true) {
			for (; last >= 0 && s[last] == '+'; last--);
			if (last < 0) {
				break;
			}
			bool f1 = false;
			for (first = 0; first < last; first++) {
				if (s[first] == '+') {
					s[first] = '-';
					f1 = true;
				} else {
					break;
				}
			}
			if (f1) {
				//printf("a1 %s\n", s);
				ans++;
			}

			std::reverse(s, s + last + 1);

			ans++;
			for (int i = 0; i < last + 1; i++) {
				if (s[i] == '+') s[i] = '-';
				else if (s[i] == '-') s[i] = '+';
			}
			//printf("a2 %s\n", s);
		}

		printf("Case #%d: %d\n", casenum++, ans);
		fflush(stdout);
	}
	return 0;
}
