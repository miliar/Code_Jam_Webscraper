#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int t,ctr,m,n,i,j,temp,min,a,b,x,y;
	vector<vector<int> > arr;
	scanf("%d",&t);
	for(ctr=1;ctr<=t;ctr++)
	{
		arr.clear();
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
		{
			arr.push_back(vector<int>());
			for(j=0;j<n;j++)
			{
				scanf("%d",&temp);
				arr[i].push_back(temp);
			}
		}
		
		while(1)
		{
			min = 2000000000;
			x = y = 0;
			for(i=0;i<arr.size();i++)
			{
				for(j=0;j<arr[0].size();j++)
				{
					if(min>arr[i][j])
					{
						
						a = i;
						b = j;
						min = arr[i][j];
						//printf("%d %d",a,b);
					}
				}
				//printf("\n");
			}
			
			//printf("%d %d\n",a,b);
			for( i=0;i<arr.size();i++)
			{
				if(arr[i][b] == min)
				{
					x++;
				}
			}
			
			for( i=0;i<arr[a].size();i++)
			{
				if(arr[a][i] == min)
				{
					y++;
				}
			}
			
			if(x!=arr.size() && y!=arr[a].size())
			{
				printf("Case #%d: NO\n",ctr);
				break;
			}
			
			else if(x==arr.size())
			{
				for(i=0;i<arr.size();i++)
				{
					arr[i].erase(arr[i].begin() + b);
				}
			}
			
			else if(y==arr[a].size())
			{
				arr.erase(arr.begin()+a);
			}
			
			if(arr.size() == 0 )break;
		}
		if(arr.size() == 0 )
		{
			printf("Case #%d: YES\n",ctr);
		}
	}

return 0;
}

