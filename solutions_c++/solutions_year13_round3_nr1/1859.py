#include<cstdio>
using namespace std;
char x[1000005];
int t, n;
char tab[] = { 'a', 'e', 'o', 'i', 'u' };
bool add( int a )
{
	for ( int i = 0; i <= 5; i ++ ) 
	{
		if ( i == 5 ) return 1;
		else 
			if ( x[a] == tab[i] ) return 0;
	}
}
void doit()
{
	int size = 0;
	while ( x[size] ) size ++;
	long long ile = 0, wynik = 0, ost = -1;
	for ( int i = 0; x[i]; i ++ )
	{
		if ( add ( i ) ) ile ++;
		else ile = 0;
		if ( ile >= n ) 
		{
			int p = i - n + 2;
			p -= ( ost + 1 );
			p *= ( size - i );
			ost = i - n + 1;
			wynik += p;
		}
// 		printf ( "i: %d ile : %d w: %d\n", i, ile, wynik );
	}
	printf ( "%lld\n", wynik );
}
int main ()
{
	scanf ( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		printf ( "Case #%d: ", i );
		scanf ( " %s %d", x, &n );
		doit();
	}
}