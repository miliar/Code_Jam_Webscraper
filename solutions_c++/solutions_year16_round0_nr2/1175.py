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

char str[1000];
int n;

int work()
{
	scanf("%s", str + 1);
	n = strlen(str + 1);
	int cnt = 1;
	rep(i, 2, n)
		if (str[i] != str[i - 1]) ++cnt;
	if (str[1] == '-')
		return (cnt + 1) / 2 * 2 - 1;
	else
		return cnt / 2 * 2;
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
		printf("Case #%d: %d\n", _, work());
	return 0;
}
