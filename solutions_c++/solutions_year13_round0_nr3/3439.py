#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool isPalin(int number);

int main(void)
{
	int n, i;
	int A, B, a, b;
	int power=1;

	FILE *in = fopen("C-small-attempt2.in", "r");
	FILE *out = fopen("C-small-attempt2.out", "w");

	fscanf(in, "%d ", &n);
	for ( i=1; i<=n; i++ )
	{
		int count=0;
		fscanf(in, "%d %d ", &A, &B);
		// a, b는 A, B의 루트

		for ( int j=1; j<=B; j++ )
		{
			if ( j*j>B ) break;
			if ( j*j >= A && isPalin(j) && isPalin(j*j) )
				count++;
		}

		fprintf(out, "Case #%d: %d\n", i, count);
	}
	return 0;
}

bool isPalin(int number)
{
	char arr[10]={0};

	itoa(number, arr, 10);
	for ( int i=0; i<strlen(arr)/2; i++ )
	{
		if ( arr[i] != arr[strlen(arr)-1-i] )
			return false;
	}
	return true;
}