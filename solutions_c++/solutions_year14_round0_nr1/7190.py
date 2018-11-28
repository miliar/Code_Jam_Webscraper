#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
using namespace std;
int main()
{
	int t=0,order=1,a[5][5],temp[3][5];
	int cnt=0,element;
	short i,j,ans;
	scanf("%d",&t);
	int test;
	for(test=1;test<=t;test++)
	{
        while(order<3)
		{
			scanf("%d",&ans);
			for(i=1; i<5; i++)
				for(j=1; j<5; j++)
					scanf("%d",&a[i][j]);

			for(i=1; i<5; i++)
				temp[order][i]=a[ans][i];
			order++;
		}

		order=1;
		for(i=1; i<5; i++)
		{
			for(j=1; j<5; j++)
			{
				if(temp[1][i]==temp[2][j])
				{
					cnt++;
					element=temp[1][i];
				}
			}
		}

		if(cnt==1)
			printf("Case #%d: %d\n",test,element);
		else if(cnt>1)
			printf("Case #%d: Bad magician!\n",test);
		else if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",test);

		cnt=0;


        
	}

}
