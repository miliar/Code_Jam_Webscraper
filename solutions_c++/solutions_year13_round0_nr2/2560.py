#include<iostream>
#include<cstdio>
using namespace std;
int t[102][104];
int a,b,c,d,n,m,z;
int poz[104];
int pio[103];
bool ok;
main()
{
scanf("%d",&z);
for(int u=1;u<=z;u++)
	{
	for(int i=0;i<=100;i++){poz[i]=0;pio[i]=0;}
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)
		{
		for(int j=1;j<=m;j++)
			{
			scanf("%d",&t[i][j]);
			poz[i]=max(poz[i],t[i][j]);
			pio[j]=max(pio[j],t[i][j]);
			}
		
		}
	ok=1;
	for(int i=1;i<=n;i++)
		{
		for(int j=1;j<=m;j++)
			{
			if(poz[i]>t[i][j]&&pio[j]>t[i][j])ok=0;
			}
		}
	printf("Case #%d: ",u);
	printf(ok?"YES\n":"NO\n");	
	}
}	
