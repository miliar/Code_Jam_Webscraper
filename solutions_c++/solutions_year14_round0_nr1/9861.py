#include<iostream>

using namespace std; 

int main()
{
	freopen("test.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int t,cas=1;
	scanf("%d",&t);
	
	while (t--)
	{
		int a[4][4],b[4][4],r1,r2,c,i,count=0,e;
		scanf("%d",&r1);
		r1--;
		for(i=0;i<4;i++)
		{
			for(c=0;c<4;c++)
			{
				scanf("%d",&a[i][c]);
			}
		}
		scanf("%d",&r2);
		r2--;
		for(i=0;i<4;i++)
		{
			for(c=0;c<4;c++)
			{
				scanf("%d",&b[i][c]);
			}
		}
		
		for(i=0;i<4;i++)
		{
		
			for(c=0;c<4;c++)
			{
				if(a[r1][i]==b[r2][c])
				{
					count+=1;
					e=a[r1][i];
				}
			}
		}

		if(count==1)
			printf("Case #%d: %d\n",cas,e);
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",cas );
		if(count>1)
			printf("Case #%d: Bad magician!\n",cas );



		cas++;
	}
	return 0; 

} 