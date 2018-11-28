//Problem A. Magic Trick CODEJAM2014
#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
	//fstream myfile(""C:\Users\gautam.gautam-pc\Documents\Code\A-small-attempt0.in"", ios_base::in);

	int t,caseno=0;
	scanf("%d", &t);
	while(t--)
	{
		caseno++;
		int A[4][4],B[4][4],Common[4],row1,row2,answer=0,k=0;
		scanf("%d", &row1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d", &A[i][j]);
			}
		}
		scanf("%d", &row2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d", &B[i][j]);
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(A[row1-1][i]==B[row2-1][j])
				{
					answer++;
					Common[k++]=A[row1-1][i];
					break;
				}
			}
		}
		if(answer==1)
		{
			printf("Case #%d: %d\n", caseno, Common[0]);
		}
		else if(answer>1)
		{
			printf("Case #%d: Bad magician!\n", caseno);
		}
		else
		{
			printf("Case #%d: Volunteer cheated!\n", caseno);
		}
	}
}
