#include <stdio.h>
#include <string.h>

int main(void)
{
	int n, m, t, i;
	int newarr[100][100];

	int colmax[100];
	int rowmax[100];
	int max;

	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.out", "w");

	fscanf(in, "%d ", &t);
	for ( i=1; i<=t; i++ )
	{
		int arr[100][100]={0};
		char YES[5]={0};

		strcpy(YES, "YES");

		fscanf(in, "%d %d ", &n, &m);
		
		for ( int a=0; a<n; a++ )
			for ( int b=0; b<m; b++ )
			{
				fscanf(in, "%d ", &arr[a][b]);
				newarr[a][b]=100;
			}
		
		if ( n > m ) max = n;
		else max = m;

		for ( int a=0; a<max; a++ )
		{
			colmax[a] = arr[0][a];
			rowmax[a] = arr[a][0];
			for ( int b=0; b<max; b++ )
			{
				if ( colmax[a] < arr[b][a] )
					colmax[a] = arr[b][a];
				
				if ( rowmax[a] < arr[a][b] )
					rowmax[a] = arr[a][b];
			}
		}

		//col is down

		for ( int a=0; a<max; a++ )
		{
			for ( int b=0; b<max; b++ )
			{
				if ( newarr[a][b] > colmax[b] && colmax[b] != 0 )
					newarr[a][b] = colmax[b];

				if ( newarr[a][b] > rowmax[a] && rowmax[a] != 0 )
					newarr[a][b] = rowmax[a];
			}
		}

		int flag=0;
		for ( int a=0; a<n; a++ )
		{
			for ( int b=0; b<m; b++ )
			{
				if ( arr[a][b] != newarr[a][b] )
				{
					flag=1;
					break;
				}
			}
			if ( flag == 1 ) break;
		}
		if ( flag == 1 ) strcpy(YES, "NO");

		fprintf(out, "Case #%d: %s\n", i, YES);
	}

	fclose(in);
	fclose(out);
	return 0;
}