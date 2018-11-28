#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
long long palindrome[50];
long long A, B;
int T, n;

bool isPalindrome(long long number)
{
	char a[20], b[20];
	int k = 0;

	while (number)
	{
		a[k++] = number % 10 + '0';
		number /= 10;
	}
	a[k] = '\0';

	strcpy(b, a);
	strrev(b);

	return (strcmp(b, a) == 0);
}

void generatePalindromes()
{
	int a = 1;
	int b = 10000000;

	for (long long i = a; i <= b; i++)
	{
		if (!isPalindrome(i))	continue;

		long long square = (long long) (i * i);

		if (isPalindrome(square))	palindrome[n++] = square;
	}
}

void solve(int testCase)
{
	int sol = 0;
	
	for (int i = 0; i < n && palindrome[i] <= B; i++)
		if (palindrome[i] >= A)
			sol++;

	printf ("Case #%d: %d\n", testCase, sol);
}


int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	scanf ("%d", &T);
	generatePalindromes();

	for (int i = 1; i <= T; i++)
	{
		scanf ("%lld%lld", &A, &B);
		solve(i);
	}

	return 0;
}