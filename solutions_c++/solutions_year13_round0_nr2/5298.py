#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define PB push_back

const int MAXN = 100, INF = 1000;


int tab[MAXN + 1][MAXN + 1], hor[MAXN + 1], ver[MAXN + 1];
int t, n, m;


void testcase(int q)
{
	for(int i = 1 ; i <= n ; i++)
	{
		for(int j = 1 ; j <= m ; j++)
		{
			scanf("%d", &tab[i][j]);
		}
	}
	for(int i = 1 ; i <= n ; i++)
	{
		int tmp = -1;
		for(int j = 1 ; j <= m ; j++)
		{
			tmp = max(tmp, tab[i][j]);
		}
		hor[i] = tmp;
	}
	for(int i = 1 ; i <= m ; i++)
	{
		int tmp = -1;
		for(int j = 1 ; j <= n ; j++)
		{
			tmp = max(tmp, tab[j][i]);
		}
		ver[i] = tmp;
	}
	bool c = false;	
	for(int i = 1 ; i <= n ; i++)
	{
		for(int j = 1 ; j <= m ; j++)
		{
			if(tab[i][j] < hor[i] && tab[i][j] < ver[j])
				c = true;
		}
	}
	if(!c)
		printf("Case #%d: YES\n", q);
	else
		printf("Case #%d: NO\n", q);
}

void clean()
{
	for(int i = 1 ; i <= n ; i++)
		for(int j = 1; j <= m ; j++)
			tab[i][j] = 0;
	for(int i = 1 ; i <= n ; i++)
		hor[i] = 0;
	for(int i = 1 ; i <= m ; i++)
		ver[i] = 0;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1 ; i <= t ; i++)
	{	
		scanf("%d%d", &n, &m);
		testcase(i);
		clean();	
	}
	return 0;
}
