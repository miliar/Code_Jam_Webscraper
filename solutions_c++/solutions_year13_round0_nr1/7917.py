#include <stdio.h>
int main()
{
	freopen("in.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, i, j, suc, draw;
	scanf("%d", &t);
	char a[4][4];
	for(i=1; i<=t; i++)
	{
		//scanf("%c%c%c%c", &a[0][0], &a[0][1], &a[0][2], &a[0][3]);
		scanf("%s", a[0]);
		//printf("%s", a[0]);
		scanf("%s", a[1]);
		//printf("%s", a[1]);
		scanf("%s", a[2]);
		//printf("%s", a[2]);
		scanf("%s", a[3]);
		//printf("%s", a[3]);
		suc = 0;
		draw = 1;
		for(j=0; j<4; j++)
		{
			if(a[j][0] == '.'  || a[j][1] == '.' || a[j][2] == '.' || a[j][3] == '.')
			{
				draw = 0;
				//printf("1-yes %d\n", i);
			}
			if((a[j][0] == 'X' || a[j][0] == 'T') && (a[j][1] == 'X' || a[j][1] == 'T') && (a[j][2] == 'X' || a[j][2] == 'T') && (a[j][3] == 'X' || a[j][3] == 'T'))
			{
				//printf("2-yes %d\n", i);
				printf("Case #%d: X won\n", i);
				suc = 1;break; 
			}
			else if((a[j][0] == 'O' || a[j][0] == 'T') && (a[j][1] == 'O' || a[j][1] == 'T') && (a[j][2] == 'O' || a[j][2] == 'T') && (a[j][3] == 'O' || a[j][3] == 'T'))
			{
				//printf("3-yes %d\n", i);
				printf("Case #%d: O won\n", i);
				suc = 1;break;
			}
			else if((a[0][j] == 'X' || a[0][j] == 'T') && (a[1][j] == 'X' || a[1][j] == 'T') && (a[2][j] == 'X' || a[2][j] == 'T') && (a[3][j] == 'X' || a[3][j] == 'T'))
			{
				//printf("4-yes %d\n", i);
				printf("Case #%d: X won\n", i);
				suc = 1;break;
			}
			else if((a[0][j] == 'O' || a[0][j] == 'T') && (a[1][j] == 'O' || a[1][j] == 'T') && (a[2][j] == 'O' || a[2][j] == 'T') && (a[3][j] == 'O' || a[3][j] == 'T'))
			{
				//printf("5-yes %d\n", i);
				printf("Case #%d: O won\n", i);
				suc = 1;break;
			}
		}
		
		if(suc == 1)
			continue;
		else
		{
			if((a[0][0] == 'X' || a[0][0] == 'T') && (a[1][1] == 'X' || a[1][j] == 'T') && (a[2][2] == 'X' || a[2][2] == 'T') && (a[3][3] == 'X' || a[3][3] == 'T'))
			{
				printf("Case #%d: X won\n", i);
				continue;
			}
			else if((a[0][0] == 'O' || a[0][0] == 'T') && (a[1][1] == 'O' || a[1][j] == 'T') && (a[2][2] == 'O' || a[2][2] == 'T') && (a[3][3] == 'O' || a[3][3] == 'T'))
			{
				printf("Case #%d: O won\n", i);
				continue;
			}
			
			else if((a[0][3] == 'X' || a[0][3] == 'T') && (a[1][2] == 'X' || a[1][2] == 'T') && (a[2][1] == 'X' || a[2][1] == 'T') && (a[3][0] == 'X' || a[3][0] == 'T'))
			{
				printf("Case #%d: X won\n", i);
				continue;
			}
			
			else if((a[0][3] == 'O' || a[0][3] == 'T') && (a[1][2] == 'O' || a[1][2] == 'T') && (a[2][1] == 'O' || a[2][1] == 'T') && (a[3][0] == 'O' || a[3][0] == 'T'))
			{
				printf("Case #%d: O won\n", i);
				continue;
			}
			
			else if(draw == 1)
				printf("Case #%d: Draw\n", i);
			else
				printf("Case #%d: Game has not completed\n", i);
		}
	}
	return 0;
}
