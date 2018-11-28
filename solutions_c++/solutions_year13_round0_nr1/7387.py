#include <cstdio>
#include <iostream>

using namespace std;

char b[10][10];

int main ()
{
	int T;
	
	scanf("%d", &T);
	
	for (int i=1; i<=T; i++)
	{
		//if (i>1)	scanf("%s", b[0]);

		for (int j=0; j<4; j++)
			scanf("%s", b[j]);

		int hasDot = 0;
		int x, o, end =0;
		
		
		
		for (int j=0; j<4; j++)
		{
			x = o = 0;
			for (int k=0; k<4; k++)
			{
				if (b[j][k] == '.')	hasDot = 1;
				x += (b[j][k] == 'X');
				x += (b[j][k] == 'T');
				o += (b[j][k] == 'O');
				o += (b[j][k] == 'T');
			}
			if (x==4)	{printf("Case #%d: X won\n", i); 	end = 1; break;}
			if (o==4)	{printf("Case #%d: O won\n", i); 	end = 1; break;}
		}
		if (end)	continue;		
		
		
		
		for (int j=0; j<4; j++)
		{
			x = o = 0;
			for (int k=0; k<4;k++)
			{
				x += (b[k][j] == 'X');
				x += (b[k][j] == 'T');
				o += (b[k][j] == 'O');
				o += (b[k][j] == 'T');
			}
			if (x==4)	{printf("Case #%d: X won\n", i); 	end = 1; break;}
			if (o==4)	{printf("Case #%d: O won\n", i); 	end = 1; break;}
		}
		if (end)	continue;	
		
		x = o = 0;
		for (int j=0; j<4; j++)
		{
			x += (b[j][j] == 'X');
			x += (b[j][j] == 'T');
			o += (b[j][j] == 'O');
			o += (b[j][j] == 'T');
		}
		if (x==4)	{printf("Case #%d: X won\n", i); 	continue;}
		if (o==4)	{printf("Case #%d: O won\n", i); 	continue;}	
		

		
		x = o = 0;
		for (int j=0; j<4; j++)
		{
			x += (b[j][3-j] == 'X');
			x += (b[j][3-j] == 'T');
			o += (b[j][3-j] == 'O');
			o += (b[j][3-j] == 'T');
		}
		if (x==4)	{printf("Case #%d: X won\n", i); 	continue;}
		if (o==4)	{printf("Case #%d: O won\n", i); 	continue;}		

		
		if (hasDot)
			printf("Case #%d: Game has not completed\n", i);
		else
			printf("Case #%d: Draw\n", i);
		

	}
	
	scanf("%s", b[0]);
	return 0;
}
	