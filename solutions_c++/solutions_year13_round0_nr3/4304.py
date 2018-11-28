#ifndef __EXCLUDE_THIS_FILE__
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>

using namespace std;

bool isPalindrome (unsigned long long int X)
{
	if (X < 10) return true;
	unsigned long long int Y = X, Temp = 0;
	while (Y)
	{
		Temp *= 10;
		Temp += (Y % 10);
		Y /= 10;
	}
	return (Temp == X);
}
unsigned long long int Start, End, Temp, Counter = 1;
set <unsigned long long int> ValidPalindromes;
int main()
{
	freopen ("Input.txt", "r", stdin);
	freopen ("Scratch.txt", "w", stdout);
	Temp = 0;
	while (Temp < 10e15)
	{
		if (isPalindrome (Counter))
		{
			Temp = Counter * Counter;
			if (isPalindrome (Temp)) ValidPalindromes.insert (Temp);
		}
		Counter++;
	}
	int total = 0;
	scanf ("%d", &total);
	for (int i = 1; i <= total; i++)
	{
		Counter = 0;
		scanf ("%lld%lld", &Start, &End);
		for (set<unsigned long long int>::iterator it = ValidPalindromes.begin(); it != ValidPalindromes.end(); ++it)
			if (*it <= End && *it >= Start) Counter++;
		printf ("Case #%d: %lld\n", i, Counter);
	}
}
#endif
