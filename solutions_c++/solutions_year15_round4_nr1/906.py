#include<cstdio>
#include<cstring>
using namespace std;
char A[128][128];
int Test,n,m;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&Test);
	for(int t=1;t<=Test;t++)
	{
		scanf("%d %d\n",&n,&m);
		for(int i=1;i<=n;i++)
			scanf("%s",A[i]+1);
		bool flag=1;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
				if(A[i][j]!='.')
				{
					int cnt=0;
					for(int k=1;k<=m;k++)
						if(A[i][k]!='.')
							cnt++;
					for(int k=1;k<=n;k++)
						if(A[k][j]!='.')
							cnt++;
					if(cnt==2)flag=0;
				}
		}
		if(!flag)
		{
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		int ans=0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			if(A[i][j]!='.'){
				if(A[i][j]=='<')
				{
					int k;
					for(k=j-1;k>0;k--)
						if(A[i][k]!='.')break;
					if(k==0) ans++;
				}
				if(A[i][j]=='>')
				{
					int k;
					for(k=j+1;k<=m;k++)
						if(A[i][k]!='.')break;
					if(k>m) ans++;
				}
				if(A[i][j]=='^')
				{
					int k;
					for(k=i-1;k>0;k--)
						if(A[k][j]!='.')break;
					if(k==0)ans++;
				}
				if(A[i][j]=='v')
				{
					int k;
					for(k=i+1;k<=n;k++)
						if(A[k][j]!='.')break;
					if(k>n)ans++;
				}
			}
		printf("Case #%d: %d\n",t,ans);
	}
}