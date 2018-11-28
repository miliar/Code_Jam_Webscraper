#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define INF 1000000000
int a[5][5];
bool chk[20];
main()
{
 	freopen("A-small-attempt0.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int t;
	int r1,r2;
	int cnt=0;
	int jum;
	scanf("%d",&t);
	int tcase=1;
	int i,j;
	while(t--)
	{
		cnt=0;
		memset(chk,0,sizeof chk);
		scanf("%d",&r1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i+1 == r1) chk[a[i][j]]=1;
			}
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i+1 == r2) 
				{
					if(chk[a[i][j]]){ cnt++; jum=a[i][j]; }
				}
			}
		}
		printf("Case #%d: ",tcase++);
		if(cnt==1) printf("%d\n",jum);
		else if(cnt>1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}

