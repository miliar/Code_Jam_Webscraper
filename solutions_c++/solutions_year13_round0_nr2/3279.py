#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int i,j,t,n,m,ca,max;
	int map[110][110];
	int num[110][110];
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&t);
	for (ca=1;ca<=t;ca++)
	{
		scanf("%d %d",&n,&m);
		for (i=0;i<n;i++) for (j=0;j<m;j++) scanf("%d",&map[i][j]);		
		for (i=0;i<n;i++)
		{
			max=0;
			for (j=0;j<m;j++) if (max<map[i][j]) max=map[i][j];
			for (j=0;j<m;j++) num[i][j]=max;
		}
		for (i=0;i<m;i++)
		{
			max=0;
			for (j=0;j<n;j++) if (max<map[j][i]) max=map[j][i];
			for (j=0;j<n;j++) if (num[j][i]>max) num[j][i]=max;
		}
		for (i=0;i<n;i++)
		{
			j=0;
			while (j<m&&num[i][j]==map[i][j]) j++;			
			if (j<m) {printf("Case #%d: NO\n",ca);break;} 
		}
		if (i>=n) printf("Case #%d: YES\n",ca);
	}
	return 0;
}
			