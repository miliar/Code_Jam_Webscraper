#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
char s[6][6];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	int T, ca = 1;
	cin >> T;
	while ( T -- )
	{
		for ( int i= 0;i<4;i++ ) scanf("%s",s[i]);
		printf("Case #%d: ",ca ++);
		int fg = 0,bb = 1;
		for(int i =0;i<4;i++) 
		{
			if(s[i][i]!='X'&&s[i][i]!='T')
			{
				bb=0;
				break;
			}
		}
		if(bb)
		{
			printf("X won\n");
			continue;
		}
		bb=1;
		for(int i =0;i<4;i++) 
		{
			if(s[i][4-i-1]!='X'&&s[i][4-i-1]!='T')
			{
				bb=0;
				break;
			}
		}
		if(bb)
		{
			printf("X won\n");
			continue;
		}
		fg=0;
		for(int i= 0;i<4;i++)
		{
			bb=1;
			for(int j=0;j<4;j++)
			{
				if(s[i][j]!='X'&&s[i][j]!='T')
				{
					bb=0;
					break;
				}
			}
			if(bb)
			{
				fg=1;
				break;
			}
		}
		if(fg)
		{
			printf("X won\n");
			continue;
		}
		fg=0;
		for(int i= 0;i<4;i++)
		{
			bb=1;
			for(int j=0;j<4;j++)
			{
				if(s[j][i]!='X'&&s[j][i]!='T')
				{
					bb=0;
					break;
				}
			}
			if(bb)
			{
				fg=1;
				break;
			}
		}
		if(fg)
		{
			printf("X won\n");
			continue;
		}
		// OOOOOOO
		bb = 1;
		for(int i=0;i<4;i++) 
		{
			if(s[i][i]!='O'&&s[i][i]!='T')
			{
				bb=0;
				break;
			}
		}
		if(bb)
		{
			printf("O won\n");
			continue;
		}
		bb=1;
		for(int i =0;i<4;i++) 
		{
			if(s[i][4-i-1]!='O'&&s[i][4-i-1]!='T')
			{
				bb=0;
				break;
			}
		}
		if(bb)
		{
			printf("O won\n");
			continue;
		}
		fg=0;
		for(int i= 0;i<4;i++)
		{
			bb=1;
			for(int j=0;j<4;j++)
			{
				if(s[i][j]!='O'&&s[i][j]!='T')
				{
					bb=0;
					break;
				}
			}
			if(bb)
			{
				fg=1;
				break;
			}
		}
		if(fg)
		{
			printf("O won\n");
			continue;
		}
		fg=0;
		for(int i= 0;i<4;i++)
		{
			bb=1;
			for(int j=0;j<4;j++)
			{
				if(s[j][i]!='O'&&s[j][i]!='T')
				{
					bb=0;
					break;
				}
			}
			if(bb)
			{
				fg=1;
				break;
			}
		}
		if(fg)
		{
			printf("O won\n");
			continue;
		}
		fg=0;
		for(int i= 0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(s[i][j]=='.') fg=1;
			}
		}
		if(fg) puts("Game has not completed");
		else puts("Draw");
	}
	return 0;
}

