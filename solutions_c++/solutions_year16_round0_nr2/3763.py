#include <stdio.h>
#include <string.h>

void invert( char * str )
{
	int i = 0;
	while( str[i] != '\0' )
	{
		if( str[i] == '+' )
		{
			str[i] = '-';
		}
		else
		{
			str[i] = '+';
		}

		i = i + 1;
	}
}

void flip( char * p, int f )
{
	int i;
	int j;
	char temp[100];	

	strncpy( temp , p , f+1);
	temp[f+1] = '\0';
	invert(temp);

	j = f;
	for( i = 0; i <= f; i = i +1)
	{
		p[i] = temp[j];
		j = j -1;
	}	

}

int check ( char * p , int s )
{
	int i;
	for( i = s ; i >= 0; i = i -1)
	{
		if( p[i] == '-')
		{
			return i;
		}
	}
	return -1;
}


int start( char * p , int s , int f , int best )
{
	int i;
	int beg;
	int curr;
	int done = check( p , s);
	char temp[101]; 

	if( done == -1 )
	{
		return f;		
	}

	if( f > best )
	{
		return 200;
	}	

	for( i = done ; i >= 0; i = i - 1 )
	{
		strcpy( temp , p ) ;

		beg = 0;
		if( temp[beg] == '+')
		{
			while( temp[beg+1] == '+'){beg++;}		
			flip( temp, beg );	
			curr = start( temp , s , f + 1 , best );			
			if( curr < best)
			{	
				best = curr;
				break;
			}
		}
		else
		{
			flip( temp , i );
			if( strcmp( temp , p ) != 0 )
			{
				curr = start( temp , s , f + 1 , best );			
				if( curr < best)
				{	
					best = curr;
					break;
				}
			}
		}
	}	

	return best;

}


int main ()
{
	int t;
	int i;
	int s;
	int best;
	char p[101];

	scanf( "%d" , &t );

	for( i = 1; i <= t; i = i +1)
	{
		scanf( "%s" ,  p );
		s = strlen( p );
		best = s * 2;
		printf( "Case #%d: %d\n" , i , start( p , s , 0 , best) );
	}
}
