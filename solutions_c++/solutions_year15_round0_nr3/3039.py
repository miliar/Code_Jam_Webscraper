#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int Case,T,N,n,m,i,j,k;
bool f[10005][3][2][4];
char s[10005];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(Case=1;Case<=T;++Case)
	{
		scanf("%d%d",&n,&m);
		scanf("%s",s+1);
		memset(f,false,sizeof(f));
		N=n;
		for(--m;m;--m)
		{
			for(i=1;i<=n;++i)++N,s[N]=s[N-n];
		}
		n=N;
		f[0][0][0][0]=1;
		for(i=1;i<=n;++i)
		{
			if(s[i]=='i')
			{
				for(j=0;j<=2;++j)
				for(k=0;k<=1;++k)
				{
					f[i][j][k][1]=f[i-1][j][k][0];
					f[i][j][k^1][0]=f[i-1][j][k][1];
					f[i][j][k^1][3]=f[i-1][j][k][2];
					f[i][j][k][2]=f[i-1][j][k][3];
				}
			}
			if(s[i]=='j')
			{
				for(j=0;j<=2;++j)
				for(k=0;k<=1;++k)
				{
					f[i][j][k][2]=f[i-1][j][k][0];
					f[i][j][k][3]=f[i-1][j][k][1];
					f[i][j][k^1][0]=f[i-1][j][k][2];
					f[i][j][k^1][1]=f[i-1][j][k][3];
				}
			}
			if(s[i]=='k')
			{
				for(j=0;j<=2;++j)
				for(k=0;k<=1;++k)
				{
					f[i][j][k][3]=f[i-1][j][k][0];
					f[i][j][k^1][2]=f[i-1][j][k][1];
					f[i][j][k][1]=f[i-1][j][k][2];
					f[i][j][k^1][0]=f[i-1][j][k][3];
				}
			}
			f[i][1][0][0]|=f[i][0][0][1];
			f[i][2][0][0]|=f[i][1][0][2];
		}
		if(f[n][2][0][3])printf("Case #%d: YES\n",Case);
		else printf("Case #%d: NO\n",Case);
	}
}
