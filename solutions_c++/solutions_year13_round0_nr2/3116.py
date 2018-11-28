#include<iostream>

using namespace std;

int T;
bool ff;
int a[110][110];
int n,m;

bool check(int x, int y)
{
	bool tmp = 1;
	for(int i=1;i<=n;i++)
	{
		if(a[i][y]>a[x][y]) {
			tmp=0;
			break;
		}
	}
	if(tmp) return tmp;
	tmp = 1;
	for(int i=1;i<=m;i++)
	{
		if(a[x][i]>a[x][y]) {
			tmp=0;
			break;
		}
	}	
	return tmp;
}

int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d %d",&n,&m);
		for(int j=1;j<=n;j++)
			for(int k=1;k<=m;k++)
			{
				scanf("%d",&a[j][k]);
			}
		ff=1;
		for(int j=1;j<=n;j++)
		{
			for(int k=1;k<=m;k++)
			{
				if(!check(j,k)) {
					//printf("%d %d\n",j,k);
					ff=0;
					break;
				}
			}
			if(!ff) break; 
		}
		printf("Case #%d: ",i);
		if(ff)
		{
			puts("YES");
		}
		else
		{
			puts("NO");
		}
	}
	return 0;
}

