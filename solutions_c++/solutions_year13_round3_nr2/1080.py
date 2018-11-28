#include <stdio.h>

int n, m;

void input();
void output(int t);

int main()
{
	int i, T;
	
	freopen("input.txt", "r", stdin );
	freopen("output.txt", "w", stdout );

	scanf("%d" ,&T );

	for ( i=0; i<T; i++ )
	{
		input();
		output(i);
	}
}
void input()
{
	scanf("%d %d", &n, &m );
}
void output(int t)
{
	int i;
	printf("Case #%d: ", t+1);
	while ( 1 )
	{
		if ( n == 0 && m == 0 )
		{
			printf("\n");
			break;
		}
		if ( n > 0 )
		{
			printf("WE");
			n--;
		}
		else if ( n < 0 )
		{
			printf("EW");
			n++;
		}

		if ( m > 0 )
		{
			printf("SN");
			m--;
		}
		else if ( m < 0 )
		{
			printf("NS");
			m++;
		}
	}
}