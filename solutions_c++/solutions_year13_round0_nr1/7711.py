#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
#define SMALL

char c_table[4][4];
char x_table[4][4];
char o_table[4][4];

//#define LARGE
int main()
{
#ifdef SMALL
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif

	int case_n;
	char back;
	vector<char> senten;
	//printf("A");

	scanf("%d", &case_n);
	scanf("%c",&back);

	for (int i=0; i<case_n; i++)
	{
		char temp;
		bool xwin=false;
		bool owin=false;
		bool draw=true;
		bool complete=true;

		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				scanf("%c",&temp);
				c_table[x][y]=temp;
				if(c_table[x][y]=='T')
				{
					x_table[x][y]='X';
					o_table[x][y]='O';
				}
				else 
				{
					x_table[x][y]=c_table[x][y];
					o_table[x][y]=c_table[x][y];
				}
				if(c_table[x][y]=='.')
					complete=false;
			}
			scanf("%c",&temp);
		}
/*		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				printf("%c",c_table[x][y]);
			}
			printf("\n");
		}
		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				printf("%c",x_table[x][y]);
			}
			printf("\n");
		}
		printf("\n");
		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				printf("%c",o_table[x][y]);
			}
			printf("\n");
		}
		printf("\n");
*/		
		if((x_table[0][0] == x_table[0][1]) && (x_table[0][0] == x_table[0][2])&&(x_table[0][0] == x_table[0][3])&&(x_table[0][0]=='X'))
		{
				draw=false;
		}
		else if((x_table[0][0] == x_table[1][1]) && (x_table[0][0] == x_table[2][2])&&(x_table[3][3] == x_table[3][3])&&(x_table[0][0]=='X'))
		{
				draw=false;
		}
		else if((x_table[0][3] == x_table[1][2])&&(x_table[0][3] == x_table[2][1])&&(x_table[0][3] == x_table[3][0])&&(x_table[0][3]=='X'))
		{
			draw=false;
		}
		else
		{
			for(int y=0;y<4;y++)
			{
				if((x_table[0][y] == x_table[1][y]) && (x_table[0][y] == x_table[2][y])&&(x_table[0][y] == x_table[3][y])&&(x_table[0][y]=='X'))

				{
					draw =false;
				}
				//if(c_table[0][y])
			}
		}
		if (draw==false)xwin=true;

		if(xwin==false)
		{
			draw =true;
			if((o_table[0][0] == o_table[0][1]) && (o_table[0][0] == o_table[0][2])&&(o_table[0][0] == o_table[0][3])&&(o_table[0][0]=='O'))
			{
				draw=false;
			}
			else if((o_table[0][0] == o_table[1][1]) && (o_table[0][0] == o_table[2][2])&&(o_table[3][3] == o_table[3][3])&&(o_table[0][0]=='O'))
			{
				draw=false;
			}
			else if((o_table[0][3] == o_table[1][2])&&(o_table[0][3] == c_table[2][1])&&(o_table[0][3] == o_table[3][0])&&(o_table[0][3]=='O'))
			{
				draw=false;
			}
			else
			{
				for(int y=0;y<4;y++)
				{
					if((o_table[0][y] == o_table[1][y]) && (o_table[0][y] == o_table[2][y])&&(o_table[0][y] == o_table[3][y])&&(o_table[0][y]=='O'))
					{
						draw =false;
					}
				}
			}
			if (draw==false)owin=true;
		}

		printf("Case #%d: ",i+1);

		if(xwin==true)printf("X won");
		else if(owin==true)printf("O won");
		else if(draw==true&&complete==true)printf("Draw");
		else if(draw==true&&complete==false)printf("Game has not completed");

		printf("\n");
		scanf("%c",&temp);

	}
	return 0;
}
