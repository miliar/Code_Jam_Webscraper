#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

#define Xplayer 0
#define Oplayer 1
int main()
{
	string v[6];
	int i,j;
	int num,p;
	scanf("%d",&num);
	for(p=0;p<num;p++)
	{

		for(i=0;i<4;i++)
			cin >> v[i];
		printf("Case #%d: ",p+1);
		int dots = 0, complete = 0, player = Xplayer ;
		int countX,countO, countdot;
		int isT = 0; 

		for(i=0;i<4;i++)
		{
			countX=countO=countdot=isT=0;
			for(j=0;j<4;j++)
			{
				if( v[i][j]=='.')
				{ dots = 1;countdot++; }
				if( v[i][j]=='O') countO++;
				if( v[i][j]=='X') countX++;
				if( v[i][j]=='T') isT=1;
			}
			if(countX + isT ==4 ){  printf("X won\n"); complete=1;}
			else if(countO + isT==4 ) { printf("O won\n"); complete=1;}
		}
		if(complete==1) continue;
		for(i=0;i<4;i++)
		{
			countX = countO = countdot = isT = 0;
			for(j=0;j<4;j++)
			{
				if( v[j][i]=='.')
				{ dots = 1;countdot++; }
				if( v[j][i]=='O') countO++;
				if( v[j][i]=='X') countX++;
				if( v[j][i]=='T') isT=1;
			}
			if(countX + isT ==4 ){  printf("X won\n");complete=1;}
			else if(countO + isT==4 ){  printf("O won\n");complete=1;}
		}
		if(complete) continue;

		countX = countO = countdot = isT = 0;
		for(i=0;i<4;i++)
		{
			if( v[i][i]=='.')
			{ dots = 1;countdot++; }
			if( v[i][i]=='O') countO++;
			if( v[i][i]=='X') countX++;
			if( v[i][i]=='T') isT=1;

		}
		if(countX + isT ==4 ){  printf("X won\n");complete=1;}
		else if(countO + isT==4 ){  printf("O won\n");complete=1;}
		if(complete) continue;

		countX = countO = countdot = isT = 0;
		for(i=0;i<4;i++)
		{
			if( v[i][3-i]=='.')
			{ dots = 1;countdot++; }
			if( v[i][3-i]=='O') countO++;
			if( v[i][3-i]=='X') countX++;
			if( v[i][3-i]=='T') isT=1;

		}
		if(countX + isT ==4 ){  printf("X won\n");complete=1;}
		else if(countO + isT==4 ){  printf("O won\n");complete=1;}
		if(complete==0) 
		{
			if(dots == 1) printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	return 0;
}

