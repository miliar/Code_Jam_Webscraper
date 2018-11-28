#include<cstdio>
#include<cstring>

const int N=110;
int n,m;
int a[N][N];

bool check(int i,int j)
{
	int t,a1=1,a2=1;
	for(t=0;t<m;t++)
		if(a[i][t]>a[i][j]) { a1=0;break;}
	for(t=0;t<n;t++)
		if(a[t][j]>a[i][j]) { a2=0;break;}
	if((a1+a2)==0) return 0;
	return 1;
}

bool cal()
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			if(check(i,j)==0) return 0;
	return 1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d%d",&n,&m);
		int i,j;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		printf("Case #%d: ",cnt);
		if(cal()) printf("YES\n");
		else printf("NO\n");
	}
}
