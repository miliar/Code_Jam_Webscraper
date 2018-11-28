#include<cstdio>
#include<algorithm>

using namespace std;

int t;
int land[101][101];
int minland[101][2];
bool check[105]= {0};
int n,m;

int main()
{
	int r,i,j,k,t;
	int mini;
	bool ch = true;
	freopen("B-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&t);
	for(r = 0 ; r < t ; r++)
	{
		scanf("%d %d",&n,&m);
		mini = 101;
		ch = true;
		
		for(i = 1 ; i <= 100 ; i++)
			check[i] = 0;
		
		for(i = 0 ; i < n ; i++)
		{
			mini = 0;
			for(j = 0 ; j < m ; j++)
			{	
				scanf("%d",&land[i][j]);
				check[land[i][j]] = 1;
				
				if(land[i][j] > mini)
					mini = land[i][j];
			}
			minland[i][0] = mini;
		}
		
		for(i = 0 ; i < m ; i++)
		{
			mini = 0;
			for(j = 0 ; j < n ; j++)
			{	
				if(land[j][i] > mini)
					mini = land[j][i];
			}
			minland[i][1] = mini;
		}
		
		for(i = 0 ; i < n ; i++)
		{
			for(j = 0 ; j < m ; j++)
			{
				if(!(land[i][j] == minland[i][0] || land[i][j] == minland[j][1]))
				{
					ch = false;
					break;
				}
			}
			
			if(!ch)
				break;
		}	
		
		if(ch)
			printf("Case #%d: YES\n",r+1);
		else
			printf("Case #%d: NO\n",r+1);
	}
	return 0;
}
