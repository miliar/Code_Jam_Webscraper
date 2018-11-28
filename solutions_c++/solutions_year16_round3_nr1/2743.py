#include <bits/stdc++.h>
using namespace std;

const int MAXN = (int)5e3 + 1;

int p[47];
int n;

inline int findMax()
{
	int id = 0;
	for (int i = 0; i < n; i++)
	{
		if (p[i] > p[id])
			id = i;
	}
	return id;
}
	
void solve(int tid)
{
	printf("Case #%d:", tid);
	memset(p, 0, sizeof(p));
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &p[i]);
	int cnt = n, id;
	while (cnt > 2)
	{
		id = findMax();
		p[id]--;
		if (p[id] == 0)
			cnt--;
		printf(" %c", char('A' + id));
	}
	bool f = false;
	int ff, ss;
	ff = ss = -1;
	for (int i = 0; i < n; i++)
	{
		if (p[i] != 0)
		{
			if (!f) 
				ff = i, f = true;
			else 
				ss = i;
		}
	}
	if (p[ff] < p[ss])
		swap(ff, ss);
	int d = p[ff] - p[ss];
	p[ff] -= d;
	for (int i = 0; i < d; i++)
		printf(" %c", char('A' + ff));
	for (int i = 0; i < p[ff]; i++)
		printf(" %c%c", char('A' + ff), char('A' + ss));
	printf("\n");
}

int main()
{
	//freopen("xxx.in", "r", stdin);
	//freopen("xxx.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
		solve(i);
	return 0;
}