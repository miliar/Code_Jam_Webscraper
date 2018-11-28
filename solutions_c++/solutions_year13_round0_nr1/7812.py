#include<stdio.h>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>

#define maxN(a,b) ((a>b)?(a):(b))
#define minN(a,b) ((a<b)?(a):(b))
#define INF (int)10e9

using namespace std;

typedef vector<int> V;
typedef pair<int,int> PII;

char board[5][5];


void input_board( ) {
	for(int i = 0 ; i < 4; i++)
		for(int j = 0 ; j <= 4; j++){
			scanf("%c", &board[i][j]);

		}
		
}

void print_board() {
	printf("printing\n");
	
	for(int i = 0 ; i < 4; i++)
		for(int j = 0 ; j <= 4; j++){
			printf("%c", board[i][j]);

		}
}

bool test1(char ch) {

	int cnt = 0;
	
	for(int i = 0; i < 4; i++) {
		cnt = 0;
		for (int j = 0; j < 4; ++j)
		{
			if(board[i][j] == ch || board[i][j] == 'T') ++cnt;
		}
		if( cnt == 4) return true;
	}

	for(int j = 0; j < 4; j++) {
		cnt = 0;
		for (int i = 0; i < 4; ++i)
		{
			if(board[i][j] == ch || board[i][j] == 'T') ++cnt;
		}
		if( cnt == 4) return true;
	}

	cnt = 0;
	for (int i = 0, j = 0; i < 4; ++i, ++j)
	{	
		if ( board[i][j] == ch || board[i][j] == 'T') 
			{
				++cnt;
			}	
		if( cnt == 4) return true;
	}


cnt = 0;
	for (int i = 0, j = 3; i < 4; ++i, --j)
	{	
		if ( board[i][j] == ch || board[i][j] == 'T') 
			{
				++cnt;
			}	
		if( cnt == 4) return true;
	}
	return false;

}

bool test_() {

	for( int i = 0; i < 4; i++){
		for (int j = 0; j < 4; ++j)
		{
			if( board[i][j] == '.') return true;
		}
	}
	return false;

}
int main() {
	int T, N;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &T);

	char ch;

	for( int i = 1; i <= T; i++){
		
		scanf("%c", &ch);
		input_board();
		//print_board();
		if ( test1('O') )
			printf("Case #%d: O won\n",i);
		else if( test1('X'))
			printf("Case #%d: X won\n",i);
		else if( test_())
			printf("Case #%d: Game has not completed\n",i);
		else 
			printf("Case #%d: Draw\n",i);			
		

	}

	return 0;
}