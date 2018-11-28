#include<stdio.h>
#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int A1[4][4], A2[4][4];
	int ans1, ans2, indexi;
	int tt=1, count=0, Test_cases,i,j, id1, id2;
	scanf("%d", &Test_cases);
	while(Test_cases--)
	{
		count = 0;
		scanf("%d",&ans1);
		id1 = ans1-1;
		for(i=0;i<4;i++)
			for(j=0 ; j< 4 ; j++)
				scanf("%d", &A1[i][j]);
	
		scanf("%d",&ans2);
		id2 = ans2-1;
		for(i=0;i<4;i++)
			for(j=0 ; j< 4 ; j++)
				scanf("%d", &A2[i][j]);

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(A1[id1][i]==A2[id2][j]) 
					indexi = i,count++;
					
		printf("Case #%d: ", tt);
		tt++;
		if(count == 1)
			 printf("%d\n", A1[id1][indexi]);
		else if(count > 1) 
			cout<<"Bad magician!"<<endl;
		else 
			cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}