#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int li[100][50], board[50][50], target;

/*void PutBoard(int n){
	memset(board, 0, sizeof(board));
	memcpy(board[0], li[0], sizeof(board[0]));
	int ri=1, ci=0;
	for(int i=1; i<n*2-1; ++i){
		int j;
		for(j=0; j<ri; j++)
		if( board[ci][j] != li[i][j] )	break;
		
		if( j==ri )	
	}
}*/

char backtrace(int index, int n, int r, int c, char chance){
	int nn = 2*n-1;
	if( index==nn ){
		if( c<n )		target = c;
		else if( r<n )	target = n+r;
		return 1;
	}
	int i;
	if( c<n ){
	for(i=0; i<r; ++i)
	if( board[i][c]	!= li[index][i] )	break;
	if( i==r ){
		for(i=r; i<n; ++i)	board[i][c] = li[index][i];
		if( backtrace(index+1, n, r, c+1, chance) )	return 1;
	}
	}
	
	if( r<n ){
	for(i=0; i<c; ++i)
	if( board[r][i] != li[index][i] )	break;
	if( i==c ){
		for(i=c; i<n; ++i)	board[r][i] = li[index][i];
		if( backtrace(index+1, n, r+1, c, chance) ) return 1;
	}
	}
	
	if( chance ){
		if( c<n ){
			target = c;
			if( backtrace(index, n, r, c+1, 0) ) return 1;
		}
		if( r<n ){
			target = n+r;
			if( backtrace(index, n, r+1, c, 0) ) return 1;
		}
	}
	return 0;
}

int main(void){
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int c, cc=0, n, cnt[2501];
	
	scanf("%d", &c);
	while( c-- ){
		scanf("%d", &n);
		for(int i=0,j=n*2-1; i<j; ++i)
		for(int k=0; k<n; ++k)	scanf("%d", &li[i][k]);
		
		/* bubble sorting */
		for(int i=0,j=n*2-1; i<j; ++i)
		for(int k=i+1; k<j; ++k){
			int a;
			for(a=0; a<n; ++a)
			if(li[i][a] != li[k][a])	break;
			if( a<n && li[i][a]>li[k][a] ){
				int tmp[50];
				memcpy(tmp, li[i], sizeof(tmp));
				memcpy(li[i], li[k], sizeof(tmp));
				memcpy(li[k], tmp, sizeof(tmp));
			}
		}
		
		memset(cnt, 0, sizeof(cnt));
		for(int i=0,j=n*2-1; i<j; ++i)
		for(int a=0; a<n; ++a)	cnt[li[i][a]]++;
		printf("Case #%d:", ++cc);
		for(int i=1; i<=2500; ++i)
		if( cnt[i]&1 )	printf(" %d", i);
		putchar('\n');
		/*memset(board, 0, sizeof(board));
		memcpy(board[0], li[0], sizeof(board[0]));
		backtrace(1, n, 1, 0, 1);
		printf("Case #%d:", ++cc);
		if( target<n ){
			for(int i=0; i<n; ++i)	printf(" %d", board[i][target]);
		}
		else{
			for(int i=0; i<n; ++i)	printf(" %d", board[target-n][i]);
		}
		putchar('\n');
		printf("%d\n", target);
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j)	printf(" %d", board[i][j]);
			putchar('\n');
		}*/
	}
	
	return 0;
}

