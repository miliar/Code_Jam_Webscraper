#include<stdio.h>
const int MAX = 10; 

char board[MAX][MAX] ;

int d[8][2] = {{0,1},{1,0},{1,1},{1,-1},{0,-1},{-1,0},{-1,-1},{-1,1}} ;
int ok(int i,int j)
{
	if(i>=0 && i<4&&j>=0 && j<4)
	return 1;
	return 0 ;
}

int count(int i,int j,int key)
{
	int c=0 ,op=4;
	
	for(int p=0;p<4;p++)
	{
		int t = 0 ;
		int sx=i,sy=j ;
		while(ok(sx,sy) && (board[sx][sy] == key || board[sx][sy] == 'T') )
		{
			t++ ;
			sx += d[p][0] ;
			sy += d[p][1] ;
		}
		sx=i,sy=j ;
		while(ok(sx,sy) && (board[sx][sy] == key || board[sx][sy] == 'T') )
		{
			t++ ;
			sx += d[p+op][0] ;
			sy += d[p+op][1] ;
		}
		t-=1 ;
		
		if(t>c) c = t ; 
	}
	
		return c ;
}

int isO()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	if(board[i][j] == 'O'&&count(i,j,board[i][j]) >= 4)
	return 1 ;
	return 0 ;
}

int isX()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	if(board[i][j]=='X'&& count(i,j,board[i][j]) >= 4)
	return 1 ;
	return 0 ;
}

int isDraw()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	if(board[i][j] == '.')
	return 0 ;
	return 1 ;
}

int main()
{
	//freopen("A-small-attempt0.in","r",stdin) ;
	//freopen("A-small-attempt0.out","w",stdout) ;
	int t ;scanf("%d" , &t) ;
	int cases = 1;
	while(t--)
	{
		for(int i=0;i<4;i++)
		scanf("%s" , board[i]);
		getchar() ;
		
		printf("Case #%d: ",cases++) ;
		
		if(isO()) printf("O won\n");
		else if(isX()) printf("X won\n") ;
		else if(isDraw())	printf("Draw\n") ;
		else	printf("Game has not completed\n") ;
	}
	return 0 ;
}
/*
6
XXXT
....
OO..
....
 
XOXT
XXOO
OXOX
XXOO
 
XOX.
OX..
....
....
 
OOXX
OXXX
OX.T
O..O
 
XXXO
..O.
.O..
T...
 
OXXX
XO..
..O.
...O
 
*/
