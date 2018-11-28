#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<math.h>
using namespace std;
int t,n,m;
int maxa[500],maxb[500],f[500][500];
int main()
{
	scanf("%d",&t);
	for (int l=1;l<=t;l++)
	{
		memset(maxa,0,sizeof(maxa));
		memset(maxb,0,sizeof(maxb));				
		memset(f,0,sizeof(f));
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
			{
				scanf("%d",&f[i][j]);
				if (f[i][j]>maxa[i]) maxa[i]=f[i][j];
				if (f[i][j]>maxb[j]) maxb[j]=f[i][j];
			}
		int p=0;
		for (int i=1;i<=n;i++)
		{
		  for (int j=1;j<=m;j++)
			if (f[i][j]<maxa[i] && f[i][j]<maxb[j]) 
			{
				p=1;
				break;
			}
		  if (p==1) break;
		}
		if (p==0) printf("Case #%d: YES\n",l);
		else printf("Case #%d: NO\n",l);
	}
	return 0;
}
