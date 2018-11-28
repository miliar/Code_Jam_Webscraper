#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define PB push_back
#define MP make_pair

#define FOR(i,l,h) for(int i=(l);i<(h);++i)
#define FORE(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define CLR(s, x) memset(s, x, sizeof(s))

#define inf (1<<29)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int main()
{
	int T; scanf("%d", &T);
	int N,X, s[10005];
	FORE(cc,1,T) {
		scanf ("%d %d", &N, &X);
		FOR(i,0,N) scanf ("%d", s+i);
		sort(s,s+N);
		int i = 0, j = N-1;
		int ans = 0;
		while (i <= j) {
			if (i == j) {
				ans += 1;
				break;
			}
			if (s[i] + s[j] <= X) {
				ans += 1;
				i++;
				j--;
			} else {
				ans += 1;
				j--;
			}
		}
		printf ("Case #%d: %d\n", cc, ans);
	}
	return 0;
}
