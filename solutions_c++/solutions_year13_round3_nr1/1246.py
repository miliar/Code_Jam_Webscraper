#include <stdio.h>
#include <string.h>

#define LEN 111

char inData[LEN];
int consonantCount[LEN];
int n;
int result;

void input();
void process();
void output( int t );
bool isVowel( char a  );

int main()
{
	int i, T;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf("%d", &T );
	for ( i=0; i<T; i++ )
	{
		input();
		process();
		output( i );
	}
	return 0;
}

void input()
{
	scanf("%s %d", &inData, &n );
}
void process()
{
	int i;
	int len = strlen ( inData );
	int startPosition;

	memset( consonantCount, 0x00, sizeof ( consonantCount ) );

	for ( i=len-1; i>=0; i-- )
	{
		if ( !isVowel(inData[i]) )
		{
			consonantCount[i] = consonantCount[i+1]+1;
		}
	}

	result = startPosition = 0;
	for ( i=0; i<len; i++ )
	{
		if ( consonantCount[i] >= n )
		{
			result += (i-startPosition+1)*( len-(i+n-1) );
			startPosition = i+1;
		}
	}
}
void output(int t)
{
	printf("Case #%d: %d\n", t+1, result );
}
bool isVowel( char a  )
{
	if ( a == 'a' || a=='e' || a=='i' || a=='o' || a=='u' )
	{
		return true;
	}
	return false;
}