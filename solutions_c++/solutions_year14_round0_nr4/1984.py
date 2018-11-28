#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))

double mass[2][10000];
int dp[1010][1010];


int main(void)
{
	int cases,cas;
	int i,j,k;
	int n;
	int ans[2];
	int ken;
	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++)
	{
		ans[0]=ans[1]=0;
		scanf("%d",&n);
	
		for(i=0;i<2;i++)
			for(j=0;j<n;j++)
				scanf("%lf",&mass[i][j]);
		sort(mass[0],mass[0]+n);
		sort(mass[1],mass[1]+n);
		
		//play war
		for(i=0,j=0,ken=0;i<n && j<n;i++)
		{
			while(j<n && mass[1][j]<=mass[0][i])
				j++;

			if(j==n)
				break;
			else 
			{
				ken++;
				j++;
			}
		}
		ans[1]=n-ken;
	
		for(j=0,i=0,ken=0;j<n && i<n;j++)
		{
			while(i<n && mass[0][i]<=mass[1][j])
				i++;

			if(i==n)
				break;
			else 
			{
				ans[0]++;
				i++;
			}
		}


		printf("Case #%d: %d %d\n",cas,ans[0],ans[1]);
	}
	return 0;
}
