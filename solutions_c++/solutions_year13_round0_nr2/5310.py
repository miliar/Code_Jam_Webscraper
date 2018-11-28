#include<iostream>
#include<cstdio>

using namespace std;

int lawn[103][103];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	int Case = 1;
	scanf("%d",&T);
	while(T--)
	{
		int N,M;
		scanf("%d %d",&N,&M);
		
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				scanf("%d", &lawn[i][j]);	
			}
		}
		int possible = true;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				int found = false;
				for(int k=0;k<N;k++)
				{
					//printf("Case #%d lawnij=%d lawnkj=%d\n",Case,lawn[i][j],lawn[k][j]);
					if(lawn[k][j]>lawn[i][j])
					{
					found=true;
					break;
					}
				}
				
				if(found)
				{
					for(int k=0;k<M;k++)
					{
						if(lawn[i][k]>lawn[i][j])
						{
							possible = false;
							break;
						}
					}
				}
				if(!possible)
				break;
			}
			if(!possible)
			break;
		}
		if(possible)
		printf("Case #%d: YES\n",Case);
		else
		printf("Case #%d: NO\n",Case);
		
		Case++;
	}
	return 0;
}
