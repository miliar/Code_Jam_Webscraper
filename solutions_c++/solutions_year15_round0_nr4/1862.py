#include <stdio.h>

using namespace std;

bool ANS[5][5][5];

void swap(int *a, int *b)
{
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}

void solve(int cc)
{
	int X, R, C;

	scanf("%d %d %d", &X, &R, &C);

	if(R>C)
		swap(&R, &C);

	if(ANS[X][R][C])
		printf("Case #%d: GABRIEL\n", cc);
	else
		printf("Case #%d: RICHARD\n", cc);

}

int main()
{
	int T, i;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	ANS[1][1][1]=1;			//1*
	ANS[2][1][1]=0;
	ANS[3][1][1]=0;
	ANS[4][1][1]=0;

	ANS[1][1][2]=1;
	ANS[2][1][2]=1;
	ANS[3][1][2]=0;
	ANS[4][1][2]=0;

	ANS[1][1][3]=1;
	ANS[2][1][3]=0;
	ANS[3][1][3]=0;
	ANS[4][1][3]=0;

	ANS[1][1][4]=1;
	ANS[2][1][4]=1;
	ANS[3][1][4]=0;
	ANS[4][1][4]=0;			//1*


	ANS[1][2][2]=1;			//2*
	ANS[2][2][2]=1;
	ANS[3][2][2]=0;
	ANS[4][2][2]=0;

	ANS[1][2][3]=1;
	ANS[2][2][3]=1;
	ANS[3][2][3]=1;
	ANS[4][2][3]=0;

	ANS[1][2][4]=1;
	ANS[2][2][4]=1;
	ANS[3][2][4]=0;
	ANS[4][2][4]=0;			//2*


	ANS[1][3][3]=1;			//3*
	ANS[2][3][3]=0;
	ANS[3][3][3]=1;
	ANS[4][3][3]=0;

	ANS[1][3][4]=1;
	ANS[2][3][4]=1;
	ANS[3][3][4]=1;
	ANS[4][3][4]=1;			//3*


	ANS[1][4][4]=1;			//4*
	ANS[2][4][4]=1;
	ANS[3][4][4]=0;
	ANS[4][4][4]=1;			//4*

	scanf("%d", &T);

	for(i=1; i<=T; i++)
		solve(i);

	return 0;
}