#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<vector>
#include<iostream>
using namespace std;


int main()
{
	int T,i;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		int j,k,F,S,a[4][4],b[4][4],c=0,ans;
		
		scanf("%d",&F);
		for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		scanf("%d",&a[j][k]);
		
		scanf("%d",&S);
		for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		scanf("%d",&b[j][k]);
		
		for(j=0;j<4;j++)
		{
			
			for(k=0;k<4;k++)
			{
				if(b[S-1][j]==a[F-1][k])
				{
					c++;
					if(c==1)
						ans=b[S-1][j];
					break;
				}
			}
		}
		printf("Case #%d: ",i);
		if(c==1)
		printf("%d\n",ans);
		else if(c==0)
		printf("Volunteer cheated!\n");
		else
		printf("Bad magician!\n");
		
	}
	return 0;
}

