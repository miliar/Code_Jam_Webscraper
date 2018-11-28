#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
void reset( int * f )
{
	for ( int i = 0; i < 10; i++)
	{
		f[i] = 0;
	}
}

bool check ( int * f , char * s )
{
	for( int i = 0; s[i] != '\0' ; i ++ )
	{
		f[ s[i]- 48 ] = 1;
	}
	for ( int i  = 0 ; i < 10 ; i ++ )
	{
		if( f[i] == 0 )
		{	
			return true;
		}
	}

	return false;
}

char * penis( long long int s , char * str)
{
	int found[10];
	int i;
	long long int n;

	if ( s == 0 ) 
	{
		strcpy( str , "INSOMNIA" );
	}
	else
	{
		reset( found );
		
		sprintf( str , "%d" , s );
		for( i = 1; check( found , str ); i ++ )
		{
			n = s * i;	
			sprintf( str , "%d" , n );
		}
		
	}
	
	return str;

} 

int main () 
{
	long long int n;
	int t;
	char str[1000];

	cin >> t;
	for( int i = 1 ; i <= t; i++)
	{
		cin >> n;
		printf( "Case #%d: %s\n" , i ,penis( n , str) );
	}
	
}
