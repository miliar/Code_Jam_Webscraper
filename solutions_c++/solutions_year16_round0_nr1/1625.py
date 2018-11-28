#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define LIMIT 1000
#define INSOMNIA -1

void check_digits (int digits_freq[10], int& found_digits, int number)
{
	while (number>0)
	{
		digits_freq[number%10]++;
		if (digits_freq[number%10]==1)
			found_digits++;
		number/=10;
	}
}

int last_number (int n)
{
	int digits_freq[10]={0};
	int found_digits=0;
	for (int i=1; i<=LIMIT; i++)
	{
		int number=n*i;
		check_digits(digits_freq,found_digits,number);
		if (found_digits==10)
			return number;
	}
	return INSOMNIA;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		int n;
		cin >> n;
		int answer = last_number(n);
		int mult;
		if (n!=0)
		mult = answer/n;
		if (answer==INSOMNIA)
			printf ("Case #%d: INSOMNIA\n",i+1);
		else
			printf ("Case #%d: %d\n", i+1, answer);

	}
}
