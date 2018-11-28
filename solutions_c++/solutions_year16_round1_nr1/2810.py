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
//-----------------------------------------------------------
//int N;
char s[MAXN];
std::list<char> ans;
int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		scanf("%s", s);
		int len = strlen(s);
		ans.clear();
		ans.push_back(s[0]);
		for(int i = 1; i < len; i++) {
			char c = s[i];
			char beg = *(ans.begin());
			if (c >= beg)
				ans.push_front(s[i]);
			else
				ans.push_back(s[i]);
		}

		printf("Case #%d: ", casenum++);
		for (std::list<char>::iterator it=ans.begin(); it!=ans.end(); ++it)
			printf("%c", *it);
		printf("\n");
		fflush(stdout);
	}
	return 0;
}
