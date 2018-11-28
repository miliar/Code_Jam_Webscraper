#include<cstdio>
using namespace std;
char x[105][105];
int row[105][2], column[105][2];
int f ( int r, int c )
{
  for ( int j = 1; j <= r; j ++ ) scanf ( " %s", x[j] + 1 );
  
  for ( int i = 1; i <= r; i ++ ) {row[i][0] = 0; row[i][1] = 0;}
  for( int j = 1; j <= c; j ++ ) {column[j][0] = 0; column[j][1] = 0;}
  
  for ( int i = 1; i <= r; i ++ ) 
	for( int j = 1; j <= c; j ++ )
	{
	  if ( x[i][j] != '.' )
	  {
		row[i][1] = j;
		if ( !row[i][0] ) row[i][0] = j;
		column[j][1] = i;
		if ( !column[j][0] ) column[j][0] = i;
	  }
	}
  int ans = 0;
  for ( int i = 1; i <= r; i ++ ) 
	for( int j = 1; j <= c; j ++ )
	{
	  char z = x[i][j];
	  if ( z == '.' ) continue;
	  
	  if ( row[i][0] == row[i][1] and column[j][0] == column[j][1] ) return -1;
	  if ( z == '^' and column[j][0] == i ) ans ++;
	  if ( z == 'v' and column[j][1] == i ) ans ++;
	  if ( z == '<' and row[i][0] == j ) ans ++;
	  if ( z == '>' and row[i][1] == j ) ans ++;
	}
  return ans;
}
int main ()
{
  int t;
  scanf ( "%d", &t );
  for ( int i = 1; i <= t; i ++ )
  {
	int r, c;
	scanf ( "%d %d", &r, &c );
	int ans = f(r,c);
	printf ("Case #%d: ", i );
	if ( ans == -1 ) puts ( "IMPOSSIBLE" );
	else printf ("%d\n", ans );
  }
}