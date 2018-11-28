#include<iostream>

using namespace std;

int main()
{
	
	int t,a1,a2,m1[4][4],ins,m2[4][4];
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int c=0;
		cin>>a1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>m1[i][j];
		cin>>a2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>m2[i][j];
		--a1,--a2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(m1[a1][i] == m2[a2][j])
				{
					ins=m1[a1][i];	
					++c;
				}
			}
			
		}		
		if(c>1)
		{
			printf("Case #%d: Bad magician!\n",k+1);
			continue;
		}
		if(c==1)
		{
			
			printf("Case #%d: %d\n",k+1,ins);
			continue;
		}
		printf("Case #%d: Volunteer cheated!\n",k+1);
	}
}
