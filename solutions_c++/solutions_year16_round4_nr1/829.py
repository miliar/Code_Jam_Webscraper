#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<char> memoi[3][12];

int n, r, p, s;

int chtoidx(char ch)
{
	if (ch == 'P') return 0;
	else if (ch == 'R') return 1;
	else if (ch == 'S') return 2;
}

vector<char> D(char ch, int n)
{
	if (n == 0) return{ ch };
	int idx = chtoidx(ch);
	if (memoi[idx][n].empty() || n >= 10)
	{
		vector<char> a1, a2;
		if (ch == 'P')
		{
			a1 = D('P', n - 1);
			a2 = D('R', n - 1);
		}
		else if (ch == 'R')
		{
			a1 = D('R', n - 1);
			a2 = D('S', n - 1);
		}
		else
		{
			a1 = D('S', n - 1);
			a2 = D('P', n - 1);
		}
			
		if (a1 > a2) swap(a1, a2);

		a1.insert(a1.end(), a2.begin(), a2.end());

		if (n >= 10) return a1;

		memoi[idx][n] = a1;
	}
	return memoi[idx][n];
}

vector<char> process(char ch)
{
	vector<char> ret = D(ch, n);
	int pp = 0, rr = 0, ss = 0;
	for (int i = 0; i < ret.size(); i++)
	{
		if (ret[i] == 'P') pp++;
		if (ret[i] == 'R') rr++;
		if (ret[i] == 'S') ss++;
	}

	if (pp == p && rr == r && ss == s)
	{
		return ret;
	}

	return{'Z'};
}

int main()
{
	freopen(R"(C:\Users\Unused\Downloads\A-large (1).in)", "r", stdin);
	freopen(R"(C:\Users\Unused\Downloads\A-large.out)", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d%d%d%d", &n,&r,&p,&s);

		vector<char> ans = process('P');
		vector<char> ans2 = process('R');
		vector<char> ans3 = process('S');

		if (ans > ans2) swap(ans, ans2);

		if (ans2 > ans3) swap(ans2, ans3);
		if (ans > ans2) swap(ans, ans2);

		if (ans[0] == 'Z')
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			for (int i = 0; i < ans.size(); i++)
			{
				printf("%c", ans[i]);
			}
			printf("\n");
		}
	}
}
