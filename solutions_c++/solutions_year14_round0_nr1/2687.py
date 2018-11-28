#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
int T,n,i,j,t,ans,k,tot,f[25];
int main()
{	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	for (scanf("%d",&T);T;T--)
	{	memset(f,0,sizeof(f));
		printf("Case #%d: ",++tot);
		scanf("%d",&n);
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
			{	scanf("%d",&t);
				if (i+1==n) f[t]++;
				} ans=0;
		scanf("%d",&n);
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
			{	scanf("%d",&t);
				if (i+1==n) if (f[t]) ans++,k=t;
				}
		if (ans==1) printf("%d\n",k);
		else if (ans==0) printf("Volunteer cheated!\n"); else
		printf("Bad magician!\n");
		}
	return 0;
}
