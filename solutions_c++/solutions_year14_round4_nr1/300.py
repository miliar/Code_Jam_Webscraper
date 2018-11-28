#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int N, X, A[10005];
bool flag[10005];

int main()
{
	freopen("p1.in","r",stdin);
	freopen("p1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&N,&X);
		/*tank.clear();
		for (int i=1;i<=N;i++)
		{
			int x;
			scanf("%d",&x);
			tank.insert(x);
		}
		int cnt(0);
		for (set<int>::iterator i=tank.begin();i!=tank.end();)
		{
			int now(*i);
			set<int>::iterator tmp(i);
			i++;
			tank.erase(tmp);
			cnt++;
			set<int>::iterator j=tank.upper_bound(X-now);
			if (j==tank.begin()) continue;
			j--;
			if (i==j) break;
			tank.erase(j);
		}*/
		int cnt(0);
		for (int i=1;i<=N;i++) scanf("%d",&A[i]);
		sort(A+1,A+N+1);
		memset(flag,0,sizeof flag);
		for (int i=1,j=N;i<=N;i++) if (!flag[i])
		{
			cnt++;
			while (j && A[j]+A[i]>X) j--;
			flag[i]=true;
			flag[j]=true;
			if (j) j--;
		}
		printf("Case #%d: %d\n",tt,cnt);
	}
	return 0;
}

