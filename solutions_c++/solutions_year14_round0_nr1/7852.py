#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string>

#define FORr(i,A,B)	for (int i=(A); i<(B); ++i)
#define FOR(i, N)	FORr(i,0,N)

#define PINT(I)		printf( ",%d", I )

using namespace std;

int 	get_int()		{int a; 	scanf("%d", &a); 	return a;}
double	get_double()	{double a;	scanf("%lf", &a);	return a;}
char	get_char()		{char c; 	scanf("%c", &c); 	return c;}

char str_buf[100000];
string	get_str()		{scanf("%s", str_buf); return str_buf;}

void solve()
{
	int list[4];

	int answer = -1;

	int target_row1 = get_int();
	FOR(row, 4){
		FOR( col, 4 ) {
			int num = get_int();
			if ( row + 1 != target_row1 ) continue;
			list[ col ] = num;
		}
	}
	int target_row2 = get_int();
	FOR( row, 4 ) FOR(col, 4 ) {
		int num = get_int();
		if ( row + 1 != target_row2 ) continue;
		FOR(i,4) {
			if ( num == list[i] ) {
				if ( answer == -1 ) answer = num;
				else if ( answer > 0 ) answer = -2;
			}
		}
	}
	if ( answer == -1 ) {
		printf( "Volunteer cheated!" );
	}
	else if ( answer == -2 ) {
		printf( "Bad magician!" );
	}
	else {
		printf( "%d", answer );
	}
}

int main()
{
	int T = get_int();

	FOR (t, T)
	{
		printf("Case #%d: ", t + 1);
		solve();
		printf("\n");
	}
}
