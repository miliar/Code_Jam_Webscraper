#include <stdio.h>

#include <string.h>

bool check(char a[4][4], char t);
bool bl = true, b2 = false;
int k = 1;
int m,n;

int main()

{

	char a[4][4];
	char c1,c2;
	
	int i, j, t;
	i = j = t = 0;
	int p = 4;
	
	scanf("%d", &t);
	while(t-- > 0)
	{
		
			memset(a,0,sizeof(a));
			bl = true, b2 = false;
			
			scanf("%s\\n", a[0]);
			
			scanf("%s\\n", a[1]);
			scanf("%s\\n", a[2]);
			scanf("%s\\n", a[3]);
			
		
			
			if(check(a,'O') == true)
				continue;
			else if(check(a,'X') == true)
				continue;
			if(!b2)
			{
				// draw
				printf("Case #%d: Draw\n", k++);
				continue;

			}
			else
			{
				//not
				printf("Case #%d: Game has not completed\n", k++);
				continue;
			}




	}
	return 0;
}

bool check(char a[4][4], char t)
{
	int i,j;
			for(i = 0; i <= 3; i++)
				for(j = 0; j<= 3; j++)
				{
					if(a[i][j] == '.')
						b2 = true;
					else if(a[i][j] == 'T')
					{
						a[i][j] = t;
						m=i;
						n=j;
					}

				}
			for(i = 0; i <= 3; i++)
			{
				if(((a[i][1] == a[i][2]) && ( a[i][2]==a[i][3]) && (a[i][3] ==a[i][0]) && (a[i][0] == t ) )|| ((a[0][i] == a[1][i]) && ( a[1][i]==a[2][i])&&(a[2][i] ==a[3][i] )&& (a[3][i]== t )))
				{
					//t won
					printf("Case #%d: %c won\n", k++, t);
					return true;

				}
			}
			if(((a[1][1] == a[2][2] )&&(a[2][2]== a[3][3])&&(a[3][3] == a[0][0])&&(a[0][0] == t)) || ((a[0][3] == a[1][2])&&( a[1][2] == a[3][0] )&&(a[3][0]== a[2][1])&&(a[2][1] == t)))
			{	// t won
				printf("Case #%d: %c won\n", k++, t);
				return true;
			}
			a[m][n] = 'T';
			



	return false;

}