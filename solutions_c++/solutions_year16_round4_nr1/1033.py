#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
using namespace std;

string dfs(int n, int tj)
{
	if (n == 1)
	{
		if (tj == 1) return "PS";
		if (tj == 2) return "RS";
		if (tj == 3) return "PR";
	}
	else
	{
		string p = dfs(n - 1, (tj + 0) % 3 + 1);
		string q = dfs(n - 1, (tj + 1) % 3 + 1);
		string pq, qp;
		pq = p + q;
		qp = q + p;
		if (pq < qp) return pq;
		else return qp;
	}
}
int main()
{
	int n;
	int r, p, s;
	int t, tv;
	tv = 0;
	//freopen("A-small-attempt2.in","rt",stdin);
	//freopen("A-small-attempt2.out","wt",stdout);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	scanf("%d", &t);
	while (t--)
	{
		scanf("%d", &n);
		scanf("%d %d %d", &r, &p, &s);
		int m = 1 << n;
		int a, b, c;
		a = b = 1; c = 0;
		int i, j;
		for (i = 1; i < n; i++)
		{
			j = b + c;
			c = 2 * a;
			a = b = j;
		}
		int tj = 0;
		if (r == p && s == c)
		{
			tj = 3;
		}
		else if (p == s && r == c)
		{
			tj = 1;
		}
		else if (s == r && p == c)
		{
			tj = 2;
		}

		tv++;
		printf("Case #%d: ", tv);

		if (tj == 0)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			string res = dfs(n, tj);
			printf("%s\n", res.c_str());
		}
		printf("\n");
	}
}