#include<bits/stdc++.h>
using namespace std;
double ans,tmp;
int n,m;
bool flag[50],flag2[50];
double a[100];
void calc(int i,int j)
{
	if (i == n)
	{
		if (j > 0) return;
		double ret = 1;
		for (int k=0;k<n;k++)
			if (flag[k])
				if (flag2[k]) ret*=a[k];
				else ret*=(1-a[k]);
		tmp += ret;
		return;
	}
	if (j == 0 || flag[i]==false) {
		calc(i+1,j);
		return;
	}
	flag2[i] = true;
	calc(i+1,j-1);
	flag2[i] = false;
	calc(i+1,j);
}
void dfs(int i,int j)
{
	if (i == n)
	{
		if (j > 0) return;
		tmp = 0;
		calc(0,m/2);
		ans = max(ans,tmp);//calc();
		return;
	}
	if (j == 0) {
		dfs(i+1,j);
		return;
	}
	flag[i] = true;
	dfs(i+1,j-1);
	flag[i] = false;
	dfs(i+1,j);
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T,test = 0;
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			scanf("%lf",a + i);
		ans = 0;
		dfs(0,m);
		printf("Case #%d: %.7lf\n",++test,ans);
					
	}
	
	
}
