#include<iostream>
#include<cstdlib>
#include<cstdio>

int A1[5][5],B1[5][5];

int main()
{
	int T1,i1,j1,k1,a1,b1,count1,flag1;
	scanf("%d",&T1);
	for(k1=1;k1<=T1;k1++)
	{
		int num1;
		count1=0;
		flag1=0;
		scanf("%d",&a1);
		for(i1=0;i1<4;i1++)
			for(j1=0;j1<4;j1++)
				scanf("%d",&A1[i1][j1]);
		scanf("%d",&b1);

		for(i1=0;i1<4;i1++)
			for(j1=0;j1<4;j1++)
				scanf("%d",&B1[i1][j1]);

		for(i1=0;i1<4;i1++)
			for(j1=0;j1<4;j1++)
				if(A1[a1-1][i1]==B1[b1-1][j1])
				{ count1++;
					num1=A1[a1-1][i1];
				}

			if(count1==0)
				printf("Case #%d: Volunteer cheated!\n",k1);
			else if(count1==1)
				printf("Case #%d: %d\n",k1,num1);
			else if(count1>1)
				printf("Case #%d: Bad magician!\n",k1);

	}
	return 0;
}
