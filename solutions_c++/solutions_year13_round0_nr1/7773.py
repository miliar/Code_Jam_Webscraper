#include<iostream>
#include<cassert>
#include<cstring>
#include<cstring>
#include<cstdio>
using namespace std;
char chess[5][5];
int checkx();
int checko();
int checknot();

int main()
{
	int test;
	int kk=1;
	scanf("%d",&test);
	while(test--)
	{
		
		int i,j,k;
		for(i=0;i<4;i++)
			scanf("%s",chess[i]);
		if(checkx()==1)
			printf("Case #%d: X won\n",kk);
		else if(checko()==1)
			printf("Case #%d: O won\n",kk);
		else if(checknot()==1)
			printf("Case #%d: Game has not completed\n",kk);
		else
			printf("Case #%d: Draw\n",kk);
	kk++;
	}
return 0;
}

int checkx()
{

	int i;

	for(i=0;i<4;i++)
		if((chess[i][0]=='X'||chess[i][0]=='T')&&(chess[i][1]=='X'||chess[i][1]=='T')&&(chess[i][2]=='X'||chess[i][2]=='T')&&(chess[i][3]=='X'||chess[i][3]=='T'))
		return 1;
	for(i=0;i<4;i++)
		if((chess[0][i]=='X'||chess[0][i]=='T')&&(chess[1][i]=='X'||chess[1][i]=='T')&&(chess[2][i]=='X'||chess[2][i]=='T')&&(chess[3][i]=='X'||chess[3][i]=='T'))
		return 1;
	
	if((chess[0][0]=='X'||chess[0][0]=='T')&&(chess[1][1]=='X'||chess[1][1]=='T')&&(chess[2][2]=='X'||chess[2][2]=='T')&&(chess[3][3]=='X'||chess[3][3]=='T'))
		return 1;

	else if((chess[0][3]=='X'||chess[0][3]=='T')&&(chess[1][2]=='X'||chess[1][2]=='T')&&(chess[2][1]=='X'||chess[2][1]=='T')&&(chess[3][0]=='X'||chess[3][0]=='T'))
		return 1;
	else
		return 0;
}	




int checko()
{
	int i;

	for(i=0;i<4;i++)
		if((chess[i][0]=='O'||chess[i][0]=='T')&&(chess[i][1]=='O'||chess[i][1]=='T')&&(chess[i][2]=='O'||chess[i][2]=='T')&&(chess[i][3]=='O'||chess[i][3]=='T'))
		return 1;
	for(i=0;i<4;i++)
		if((chess[0][i]=='O'||chess[0][i]=='T')&&(chess[1][i]=='O'||chess[1][i]=='T')&&(chess[2][i]=='O'||chess[2][i]=='T')&&(chess[3][i]=='O'||chess[3][i]=='T'))
		return 1;
	
	if((chess[0][0]=='O'||chess[0][0]=='T')&&(chess[1][1]=='O'||chess[1][1]=='T')&&(chess[2][2]=='O'||chess[2][2]=='T')&&(chess[3][3]=='O'||chess[3][3]=='T'))
		return 1;

	else if((chess[0][3]=='O'||chess[0][3]=='T')&&(chess[1][2]=='O'||chess[1][2]=='T')&&(chess[2][1]=='O'||chess[2][1]=='T')&&(chess[3][0]=='O'||chess[3][0]=='T'))
		return 1;
	else
		return 0;
}	

int checknot()
{

	int i,j	;

	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(chess[i][j]=='.')
				return 1;
		return 0;
}
