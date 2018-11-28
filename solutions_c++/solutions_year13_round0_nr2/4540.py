#include <cstdio>
#include <set>
using namespace std;
multiset<pair<int,pair<int,int> > >s;
int n, m, t, tab[200][200], sumy[2][200], N, M;	// 0-wiersze 1-kolumny
bool fail;
int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d %d", &n, &m);
		N=n;M=m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &tab[i][j]);
				s.insert(make_pair(tab[i][j], make_pair(i,j)));
				sumy[0][i]+=tab[i][j];
				sumy[1][j]+=tab[i][j];
			}
		fail=false;
		while (!s.empty())
		{
			pair<int,pair<int,int> > pp = *(s.begin());
			s.erase(s.begin());
			if (pp.first*n==sumy[1][pp.second.second])
			{
				for (int x = 0; x < N; x++)
				{
					if (sumy[1][pp.second.second]!=0)
						sumy[1][pp.second.second]-=tab[x][pp.second.second];
					if (sumy[0][x]!=0)
						sumy[0][x]-=tab[x][pp.second.second];
					multiset<pair<int,pair<int,int> > >::iterator it = s.find(make_pair(pp.first, make_pair(x, pp.second.second)));
					if (it!=s.end())
						s.erase(it);
				}
				m--;
			}
			else if (pp.first*m==sumy[0][pp.second.first])
			{
				for (int x = 0; x < M; x++)
				{
					if (sumy[0][pp.second.first]!=0)
						sumy[0][pp.second.first]-=tab[pp.second.first][x];
					if (sumy[1][x]!=0)
						sumy[1][x]-=tab[pp.second.first][x];
					multiset<pair<int,pair<int,int> > >::iterator it = s.find(make_pair(pp.first, make_pair(pp.second.first, x)));
					if (it!=s.end())
						s.erase(it);
				}
				n--;
			}
			else
			{
				fail=true;
				break;
			}
		}
		if (fail) printf("Case #%d: NO\n", i+1);
		else printf("Case #%d: YES\n", i+1);
		s.clear();
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 200; j++)
				sumy[i][j]=0;
	}
	return 0;
}
