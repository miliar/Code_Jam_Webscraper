#include <stdio.h>
#include <stdlib.h>

#define M 2222 // long long modulo insert!!!!!!!!!!!!
#define MODULO 1000002013

//FILE *fin = fopen("input.txt", "r" );
//FILE *fout = fopen ( "output.txt", "w" );



int n, m;
int data[M*2][3]; // [0] pos [1] people count [2] in(0) or out(1)
int dataCount;
int stack[M*2][2]; // [0] pos [1] people count
int stackCount;

long long int originalResult;
long long int changeResult;

void input();
void process();
void output( int t );

int sort_f( const void *a, const void *b );

int main()
{
	int i, T;

	freopen( "input.txt", "r",  stdin );
	freopen( "output.txt", "w", stdout );

	scanf("%d", &T );

	for ( i=0; i<T; i++ )
	{
		input();
		process();
		output( i );
	}
}

void input()
{
	int i;
	int s, e, c;

	scanf("%d%d", &n, &m );

	dataCount = originalResult = 0;
	for ( i=0; i<m; i++ )
	{
		scanf("%d %d %d", &s, &e, &c);
		if ( s!=e )
		{
			originalResult+= (((e-s-1)*(e-s)) / 2) * c;
			originalResult %= MODULO;
		}

		data[dataCount][0] = s;
		data[dataCount][1] = c;
		data[dataCount++][2] = 0;

		data[dataCount][0] = e;
		data[dataCount][1] = c;
		data[dataCount++][2] = 1;
	}
	qsort(data, m*2, sizeof ( data[0] ), sort_f );
}
void process()
{
	int i, j, temp;

	changeResult = stackCount = 0;
	for ( i=0; i<m*2; i++ )
	{
		if ( data[i][2] == 0 ) // in 
		{
			if ( stackCount != 0 && stack[stackCount-1][0] == data[i][0] )
			{
				stack[stackCount-1][1] += data[i][1];
			}
			else
			{
				stack[stackCount][0] = data[i][0];
				stack[stackCount++][1] = data[i][1];
			}
		}
		else // out
		{
			temp = stackCount;
			for ( j=temp-1; j>=0; j-- )
			{
				if ( data[i][1] == 0 ) break;

				if ( data[i][1] < stack[j][1] )
				{
					stack[j][1] -= data[i][1];

					changeResult+= (((data[i][0]-stack[j][0]-1)*(data[i][0]-stack[j][0])) / 2) * data[i][1];
					changeResult %= MODULO;

					break;
				}
				else if ( data[i][1] >= stack[j][1] )
				{
					changeResult+= (((data[i][0]-stack[j][0]-1)*(data[i][0]-stack[j][0])) / 2) * stack[j][1];
					changeResult %= MODULO;
					data[i][1] -= stack[j][1];
					stack[j][0] = stack[j][1] = 0;
					stackCount--;
				}
			}
		}
	}
}
void output( int t )
{
	long long int result;
	result = changeResult - originalResult;
	if ( result < 0 ) result += MODULO;
	printf("Case #%d: %lld\n", t+1, result );
}


int sort_f( const void *a, const void *b )
{
	int p = *(int *)a;
	int q = *(int *)b;

	if ( p == q )
	{
		p = *((int *)a+2);
		q = *((int *)b+2);
		return p-q;
	}
	else
	{
		return p-q;
	}
}