#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int map[105][105];
int n,m,ans,maxn;
int num[105];
int row[105][105],lin[105][105];
int r[105],l[105];
int main()
{	
	int t,i,j,co=0,num1;
	scanf("%d",&t);

	while(t--)
	{
		co++;num1=0;ans=0,maxn=-1;
		memset(map,110,sizeof(map));
		memset(num,0,sizeof(num));
		memset(row,0,sizeof(row));
		memset(lin,0,sizeof(lin));
		memset(l,0,sizeof(l));memset(r,0,sizeof(r));
 		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++)
			{
				scanf("%d",&map[i][j]);//cout<<map[i][j]<<' ';
				maxn=max(maxn,map[i][j]);
				
			}//cout<<endl;
		}
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++)
				for(int k=map[i][j];k<maxn;k++)
				{
					num[k]++;
			      		row[j][k]++;lin[i][k]++;
					if(row[j][k]==n) r[k]++;
				       	if(lin[i][k]==m) l[k]++;	
				}
		}
	
		printf("Case #%d: ",co);
		int flag=1;
		for(i=1;i<=maxn;i++){
		if(num[i]==0) continue;
		else {
			ans=r[i]*n+l[i]*m-r[i]*l[i];
			if(ans!=num[i])
			{flag=0;break;}
			
		}
		}
		if(flag) printf("YES\n");
		else   printf("NO\n");
	}
	return 0;
}
