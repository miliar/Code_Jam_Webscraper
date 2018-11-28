#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-small-attempt11.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int i,j,ca,t,a,b,mat1[5][5],mat2[5][5],ct,ans;
	scanf("%d",&t);
	ca=1;
	
	while(t--)
	{
		scanf("%d",&a);
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			 scanf("%d",&mat1[i][j]);
		}
		
		scanf("%d",&b);
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			 scanf("%d",&mat2[i][j]);
		}
		
		ct=0;
		for(j=0;j<4;j++)
		{
			for(i=0;i<4;i++)
			{
				if(mat1[a-1][j]==mat2[b-1][i] )
				{
					ct++;
					ans=mat1[a-1][j];
					break;
				}
			}
		}
		
		if(ct==0)
		printf("Case #%d: Volunteer cheated!\n",ca);
		
		else if(ct==1)
		 printf("Case #%d: %d\n",ca,ans);
			
		else if(ct>1)
		 printf("Case #%d: Bad magician!\n",ca);
		
		 ca++;
	}
	
	return 0;
}		 
		
