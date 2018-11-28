#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

char s[2000];
int k;

int main() {
	int tts = 0, Tests;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%s%d", s, &k);
		printf("Case #%d: ", ++tts);
		int l = strlen(s);
		int ans = 0;
		for (int i = 0; i < l; ++i) 
			if (s[i] == '-' && i + k <= l) {
				++ans;
				for (int j = i; j < i + k; ++j) 
					if (s[j] == '+') s[j] = '-'; else s[j] = '+';
			} else if (s[i] == '-') {
				ans = -1; break;
			}
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
	return 0;
}