#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
const int maxN = 205;
set<string> sen[205];
set<string> words, al, s0, s1;
map<string, int> w;
int n, cnt;

bool have(set<string> &a, string s)
{
	if (a.find(s) == a.end())
		return 0;
	return 1;
}

void init()
{
	char ch, str[105];
	scanf("%d%*c", &n);
	words.clear();
	al.clear();
	w.clear();
	cnt = 0;
	s0.clear();
	s1.clear();
	rep(i, n)
	{
		sen[i].clear();
		while (1)
		{
		scanf("%s%c", str, &ch);
		int l = strlen(str);
		string tmp = "";
		FOR(j, 0, l - 1)
			tmp += str[j];
		if (i == 2)
		{
			if (have(sen[1], tmp))
			{
				++cnt;
				al.insert(tmp);
			}
		}
		if (i > 2 && al.find(tmp) == al.end())
		{
			words.insert(tmp);
		}
		sen[i].insert(tmp);

		if (i == 1) s0.insert(tmp);
		if (i == 2) s1.insert(tmp);

		if (ch == '\n')
			break;
		}
	}

	for (typeof(words.begin()) it = words.begin(); it != words.end(); ++it)
	{
		int s = 0;
		FOR(i, 3, n) if (have(sen[i], *it))
			s = s + (1 << (i - 3));
		w[*it] = s;
	}
}

bool ck0(string str, int s)
{
	/*if (have(sen[1], str))
		return 1;
	FOR(j, 3, n) if ((((s >> (j - 3)) & 1) == 0) && have(sen[j], str))
		return 1;
	return 0;*/
	if (((~s) & w[str]) != 0)
		return 1;
	if (s0.find(str) != s0.end())
		return 1;
	return 0;
	return (~s) & w[str];
}

bool ck1(string str, int s)
{
	/*if (have(sen[2], str))
		return 1;
	FOR(j, 3, n) if ((((s >> (j - 3)) & 1) == 1) && have(sen[j], str))
		return 1;
	return 0;*/
	if ((s & w[str]) != 0)
		return 1;
	if (s1.find(str) != s1.end())
		return 1;
	return 0;
	return s & w[str];
}

int calc(int s)
{
	int ans = 0;
	for (typeof(words.begin()) it = words.begin(); it != words.end(); ++it)
	{
		//cerr << *it << endl;
		if (ck0(*it, s) && ck1(*it, s))
			++ans;
		//cerr << ans << endl;
	}
	return ans;
}

void work()
{
	int ans = 214748364;
	FOR(s, 0, ((1 << (n - 2)) - 1))
	{
		int tmp = calc(s);
		ans = min(ans, tmp);
	}
	printf("%d\n", ans + cnt);
}

int main()
{
	int ca;
	scanf("%d", &ca);
	rep(tt, ca)
	{
		cerr << tt << endl;
		init();
		printf("Case #%d: ", tt);
		work();
	}
	return 0;
}