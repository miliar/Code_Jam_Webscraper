#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;
template <class T> inline void read(T &n)
{
    char c; int flag = 1;
    for (c = getchar(); !(c >= '0' && c <= '9' || c == '-'); c = getchar()); if (c == '-') flag = -1, n = 0; else n = c - '0';
    for (c = getchar(); c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0'; n *= flag;
}
//***************************

char pattern[10000];
int n, k;
int a[10000];

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	rep(_, 1, cases)
	{
		int cnt = 0;
		scanf("%s%d", pattern + 1, &k);
		n = strlen(pattern + 1);
		rep(i, 1, n) 
			a[i] = pattern[i] == '-';
		drep(i, n, 1) 
			a[i] = a[i] ^ a[i - 1];
		rep(i, 1, n - k + 1)
			if (a[i])
				++cnt, a[i] ^= 1, a[i + k] ^= 1;
		rep(i, 1, n) 
			if (a[i]) cnt = -inf;
		printf("Case #%d: ", _);
		if (cnt < 0) puts("IMPOSSIBLE");
		else printf("%d\n", cnt);
	}
	return 0;
}
