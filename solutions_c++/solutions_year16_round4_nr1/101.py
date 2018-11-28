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
vector<pair<string, string> > ps, _ps;
string get(char fst, int N, int R, int P, int S)
{
	string cur = "";
	cur += fst;
	rep(i, 1, N)
	{
		string nxt = "";
		REP(j, 0, cur.size())
			if (cur[j] == 'S') nxt += "PS";
			else if (cur[j] == 'P') nxt += "PR";
			else if (cur[j] == 'R') nxt += "RS";
		cur = nxt;
	}
	int r = 0, p = 0, s = 0;
	REP(i, 0, cur.size())
		if (cur[i] == 'R') ++r;
		else if (cur[i] == 'P') ++p;
		else ++s;
	if (r == R && p == P && s == S)
	{
		ps.clear();
		for (int i = 0; i < cur.size(); i += 2)
		{
			string tmpx = "", tmpy = "";
			tmpx += cur[i]; tmpy += cur[i + 1];
			ps.pb(mp(tmpx, tmpy));
		}
		rep(i, 1, N - 1)
		{
			REP(j, 0, ps.size())
				if (ps[j].yy < ps[j].xx)
					swap(ps[j].xx, ps[j].yy);
			_ps.clear();
			for (int j = 0; j < ps.size(); j += 2)
				_ps.pb(mp(ps[j].xx + ps[j].yy, ps[j + 1].xx + ps[j + 1].yy));
			ps.clear();
			for (auto j:_ps) ps.pb(j);
		}
		return min(ps[0].xx + ps[0].yy, ps[0].yy + ps[0].xx);
	}
	else
		return "IMPOSSIBLE";
}

//int found = false;

//void dfs(int cur, 

string solve(int N, int R, int P, int S)
{
	string ans = "IMPOSSIBLE";
	string tmp = get('R', N, R, P, S);
	if (tmp != "IMPOSSIBLE" && (ans == "IMPOSSIBLE" || tmp < ans)) ans = tmp;
	tmp = get('P', N, R, P, S);
	if (tmp != "IMPOSSIBLE" && (ans == "IMPOSSIBLE" || tmp < ans)) ans = tmp;
	tmp = get('S', N, R, P, S);
	if (tmp != "IMPOSSIBLE" && (ans == "IMPOSSIBLE" || tmp < ans)) ans = tmp;
	return ans;
}

int main(int argc, char *argv[])
{
	int cases, N, R, P, S;
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		scanf("%d%d%d%d", &N, &R, &P, &S);
		printf("Case #%d: %s\n", _, solve(N, R, P, S).c_str());
	}
	return 0;
}
