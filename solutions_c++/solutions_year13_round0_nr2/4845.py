#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<string>
#include<set>
#include<numeric>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<bitset>
#include<queue>
#include<ctime>
#include<sstream>
#include<map>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
int nextint(){int a;scanf("%d",&a);return a;}
double nextdouble(){double a;scanf("%lf",&a);return a;}
bool equal(double a, double b){return fabs(a-b)<EPS;}
int n, m;
int getMaxInRow(vector<vector<int> > &g, int id)
{
	int res = 0;
	for(int i = 0; i < m; i++)
		res = max(res, g[id][i]);
	return res;
}
int getMaxInCol(vector<vector<int> > &g, int id)
{
	int res = 0;
	for(int i = 0; i < n; i++)
		res = max(res, g[i][id]);
	return res;
}

void cutRow(vector<vector<int> > &g, int id, int val)
{
	for(int i = 0; i < m; i++)
		g[id][i] = min(g[id][i], val);
}

void cutCol(vector<vector<int> > &g, int id, int val)
{
	for(int i = 0; i < n; i++)
		g[i][id] = min(g[i][id], val);
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t = nextint();
	for(int test = 1; test <= t; test++)
	{
		n = nextint();
		m = nextint();
		vector<vector<int> > g(n, vector<int> (m));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				g[i][j] = nextint();
		
		vector<vector<int> > res(n, vector<int> (m, 100));
		int times = 1000;
		while(times--)
		{
			for(int i = 0; i < n; i++)
			{
				int val = getMaxInRow(g, i);
				cutRow(res, i, val);
			}
			for(int i = 0; i < m; i++)
			{
				int val = getMaxInCol(g, i);
				cutCol(res, i, val);
			}
		}

		if(res == g)
			printf("Case #%d: YES\n", test);
		else
			printf("Case #%d: NO\n", test);
	}


	return 0;
}