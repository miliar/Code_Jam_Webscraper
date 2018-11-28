#include<stdio.h>
#include<iostream>
#include<conio.h>
using namespace std;
long int a[1003]; //
int main()
{
	long int sum = 0; //
	long int total_friends = 0; //
	int t, f = 1, n, i;
	cin >> t;
	while (t > 0)
	{
		memset(a, 0, sizeof(a));
		total_friends = 0;
		sum = 0;
		cin >> n;
		char string[1004]; 
		cin >> string;
		for (i = 0; i <= n; i++)
		{
			a[i] = string[i] - 48;
			if (sum < i)
			{
				total_friends = total_friends + i - sum;
				sum = i;
			}
			else
				;
			sum = sum + a[i];

		}
		printf("Case #%d: %ld\n", f++, total_friends);
		t--;
	}
	_getch();
	return 0;
}