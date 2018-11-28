/*
    Author: Zhouxing Shi
    Created on Apr11, 2014
*/
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
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;

//***************************

int N;
char s[100000];

void solve(int _)
{
	scanf("%d", &N);
	scanf("%s", s);
	int cur = s[0] - '0';
	int ans = 0;
	rep(i, 1, N)
	{
		if (cur < i) ans += i - cur, cur = i;
		cur += s[i] - '0';
	}
	printf("Case #%d: %d\n", _, ans);
}

int main()
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) solve(_); 
    return 0;
}


