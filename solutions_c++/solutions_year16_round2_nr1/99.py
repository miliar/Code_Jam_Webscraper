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

const string word[10] = 
{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int cnt[300], cr[12], cases;
string ans;
char buf[5000];

void dfs(int cur)
{
	if (ans.size()) return;
	if (cur == 10)
	{
		rep(i, 0, 25)
			if (cnt[i]) return;
		rep(i, 0, 9)
			rep(j, 1, cr[i])
				ans += char(i + '0');
		return;
	}
	int tmp[30];
	rep(i, 0, 25) tmp[i] = cnt[i];
	cr[cur] = 0;
	dfs(cur + 1);
	rep(i, 1, 3000)
	{
		int can = true;
		REP(j, 0, word[cur].size())
			if (cnt[word[cur][j] - 'A'] == 0) can = false;
		if (!can) 
		{
			rep(i, 0, 25) cnt[i] = tmp[i];
			return;
		}
		REP(j, 0, word[cur].size())
			--cnt[word[cur][j] - 'A'];
		cr[cur] = i;
		dfs(cur + 1);
	}
}

// {"ONE",  "NINE"};

void deal(int d)
{
	rep(j, 1, cr[d])
		REP(i, 0, word[d].size())
			--cnt[word[d][i]];
}

int main(int argc, char *argv[])
{
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		clr(cnt);
		scanf("%s", buf);
		for (int i = 0; buf[i]; ++i)
			cnt[buf[i]]++;
		cr[0] = cnt['Z'];
		deal(0);
		cr[6] = cnt['X'];
		deal(6);
		cr[8] = cnt['G'];
		deal(8);
		cr[2] = cnt['W'];
		deal(2);
		cr[4] = cnt['U'];
		deal(4);
		cr[3] = cnt['R'];
		deal(3);
		cr[5] = cnt['F'];
		deal(5);
		cr[7] = cnt['S'];
		deal(7);
		cr[9] = cnt['I'];
		deal(9);
		cr[1] = cnt['O'];
		deal(1);
		ans = "";
		rep(i, 0, 9)
			rep(j, 1, cr[i])
				ans += char(i + '0');
		printf("Case #%d: %s\n", _, ans.c_str());
	}
	return 0;
}
