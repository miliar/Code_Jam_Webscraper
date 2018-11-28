# include <bits/stdc++.h>
using namespace std;

int maxi;
int solve[1001][1001];
int main()
{
	int t,j,i,k;
	scanf("%d",&t);
	for(i=1;i<=1000;i++)
	{
		for(j=1;j<=1000;j++)
		{
			if(j<=i) {solve[i][j]=0;continue;}
			solve[i][j]=solve[i][1]+solve[i][j-1]+1; 
			for(k=2;k<=(j/2);k++)
			{
				solve[i][j]=min(solve[i][j],solve[i][k]+solve[i][j-k]+1);
			}	
		}
	}
	for(j=0;j<t;j++)
	{
		int d,cmin=1,smin=0,maxt,ans=1000;
		scanf("%d",&d);
		int array[d];
		for(i=0;i<d;i++)
		{
			scanf("%d",array+i);
		}
		maxt=array[0];
		for(i=1;i<d;i++) maxt=max(maxt,array[i]);
		for(cmin=1;cmin<=maxt;cmin++)
		{
			smin=0;
			for(i=0;i<d;i++)
			smin+=solve[cmin][array[i]];
			ans=min(ans,smin+cmin);
		}
		printf("Case #%d: %d\n",j+1,ans);	

	}

	
}	
