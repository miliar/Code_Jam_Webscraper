#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <cassert>
#include <ctime>
#include <sstream>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;

#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d%d", &x, &y)
#define sc_str(s) scanf("%s", s)
#define pr(x) printf("%d ", x)
#define nl() printf("\n")
#define mp(x, y) make_pair(x, y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<bool> vb;
typedef vector<vector<bool> > vvb;

vector<int> result;
int n, r, p, s;

int getWinner(int a, int b)
{
	if (a == 0) return (b == 1) ? b : a;
	if (a == 1) return (b == 2) ? b : a;
	if (a == 2) return (b == 0) ? b : a;
}

bool checkResult()
{
	vector<int> cnt(3, 0);
	for (int i = 0; i < result.size(); ++i)
		cnt[result[i]]++;
	return cnt[0] == r && cnt[1] == p && cnt[2] == s;
}

string str_res()
{
	string pattern = "RPS";

	string res;
	res.reserve(result.size());
	for (int i = 0; i < result.size(); ++i)
		res += pattern[result[i]];
	return res;
}

int losser[] = { 2, 0, 1 };


void push(int a, int b, int round = 1)
{
	if(round==n)
	{
		result.push_back(a);
		result.push_back(b);
		return;
	}
	push(a, losser[a], round+1);
	push(b, losser[b], round+1);
}

void mysort(string &s, int l, int r)
{
	if (l == r) return;
	int mid = (l + r) >> 1;
	mysort(s, l, mid);
	mysort(s, mid + 1, r);
	if (s.substr(l, mid - l + 1) > s.substr(mid + 1, r - mid))
		s = s.substr(0, l) + s.substr(mid + 1, r - mid) + s.substr(l, mid - l + 1) + s.substr(r+1);
}

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		scanf("%d%d%d%d", &n, &r, &p, &s);
		result.assign(1 << n, -1);

		vector<string> answers;

		result.clear();
		push(1, 0);
		if (checkResult())
		{
			string temp = str_res();
			mysort(temp, 0, temp.size()-1);
			answers.push_back(temp);
		}

		result.clear();
		push(0, 2);
		if (checkResult())
		{
			string temp = str_res();
			mysort(temp, 0, temp.size()-1);
			answers.push_back(temp);
		}

		result.clear();
		push(1, 2);
		if (checkResult())
		{
			string temp = str_res();
			mysort(temp, 0, temp.size()-1);
			answers.push_back(temp);
		}

		if(answers.size()>0)
		{
			printf("Case #%d: ", tt + 1);
			string ans = answers[0];
			for (int i = 0; i < answers.size(); ++i)
				ans = min(ans, answers[i]);
			printf("%s\n", ans.c_str());
		}
		else printf("Case #%d: IMPOSSIBLE\n", tt + 1);
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
#ifdef _DEBUG
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif

	return 0;
}