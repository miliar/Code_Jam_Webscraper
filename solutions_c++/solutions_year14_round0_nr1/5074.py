#include <bits/stdc++.h>

using namespace std;

int main(void)
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
		


		int t;

		cin >> t;

		int x,y;

		int temp1[4];
		int temp2[4];
		int useless[4];

		int i,j,k;

		for(k=0;k<t;k++)
		{
			cin >> x;

			for(j=0;j<4;j++)
			{
				if(j == x-1)
					scanf("%d %d %d %d",&temp1[0],&temp1[1],&temp1[2],&temp1[3]);
			
				else
					scanf("%d %d %d %d",&useless[0],&useless[1],&useless[2],&useless[3]);
			}

			cin >> y;


			for(j=0;j<4;j++)
			{
				if(j == y-1)
					scanf("%d %d %d %d",&temp2[0],&temp2[1],&temp2[2],&temp2[3]);
			
				else
					scanf("%d %d %d %d",&useless[0],&useless[1],&useless[2],&useless[3]);
			}
			

			int count = 0;
			int ans = 0;
			
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(temp1[i] == temp2[j])
						{
						count++;
						ans = temp1[i];
						}
				}
			}

			if(count ==0)
			{
				printf("Case #%d: Volunteer cheated!\n",k+1);
			}

			else if(count == 1)
				printf("Case #%d: %d\n",k+1,ans);
			else
				printf("Case #%d: Bad magician!\n",k+1);

		}	

	}
