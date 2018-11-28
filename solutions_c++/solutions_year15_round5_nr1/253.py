#include<cstdio>
#include<vector>
using namespace std;
const int co = 1e6+3;

int t, s, n, d, m, a, c, r, mxsal, ans;
int sal[co], pod[co], bylo[co];
vector<int> v[co];

void dfs_pod(int x)
{
	pod[x] = 1;
	for (int j = 0; j < v[x].size(); j++)
	{
		if (pod[v[x][j]] == 0)
		{
			dfs_pod(v[x][j]);
			pod[x] += pod[v[x][j]];
		}
	}
}

int dfs(int x, int p)
{
	
	//printf("wchodze do %d, sal %d, p %d, pod %d\n", x, sal[x], p, pod[x]);
	bylo[x] = p+1;
	if (sal[x] < p || sal[x] > p+d)
	return 0;
	if (pod[x] == 1)
	return 1;
	int ret = 1;
	for (int j = 0; j < v[x].size(); j++)
	{
	//	printf("%d\n", bylo[v[x][j]]);
		if (bylo[v[x][j]] != p+1)
			ret += dfs(v[x][j], p);
	}
	return ret;
}

int main ()
{
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		for (int i = 0; i < n; i++)
			pod[i] =0, bylo[i] =0, v[i].clear();
		scanf ("%d %d", &n, &d);
		scanf ("%d %d %d %d", &s, &a, &c, &mxsal);
		sal[0] = s;
		r = mxsal;
		for (int i = 1; i < n; i++)
		{
			s = (a*s+c)%r;
			sal[i] = s;
		//	printf("%d: %d\n", i, sal[i]);
		}
		scanf ("%d %d %d %d", &m, &a, &c, &r);
		for (int i = 1; i < n; i++)
		{

			m = (m*a+c)%r;
		//				printf("para %d %d m %d\n", i, m%i, m);
			v[i].push_back(m%i);
			v[m%i].push_back(i);
		}
		dfs_pod(0);
		ans = 0;
		for (int i = 0; i <= max(mxsal-1-d, 0); i++)
		{
			ans = max(ans, dfs(0, i));
	//		printf("spr: %d ans: %d\n", i, ans);
		}
		printf("Case #%d: %d\n", q+1, ans);
	} 
	return 0;
	
}
