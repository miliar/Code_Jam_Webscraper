#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

void solve(int numCase)
{
	char pancakes[101], trial[101], temp;
	int answer = 0, index, half, i, length;
	bool match;

	scanf("%s", pancakes);
	length = strlen(pancakes);
	for (i = 0; i < length; i++)
		trial[i] = '+';
	trial[i] = 0;

	match = false;
	index = length - 1;	
	while (index >= 0 && !match)
	{	
		while (index >= 0 && pancakes[index] == trial[index]) index--;

		if (index != - 1)
		{
			half = index / 2;
			for (i = 0; i <= half; i++)
			{
				temp = trial[i];
				trial[i] = trial[index - i];
				trial[index - i] = temp;

				if (trial[i] == '-') trial[i] = '+';
				else trial[i] = '-';

				if (i != index - i)
				{
					if (trial[index - i] == '-') trial[index - i] = '+';
					else trial[index - i] = '-';
				}
			}
			answer++;
			index--;
		}

		match = true;
		for (i = 0; i < length; i++)
		{
			if (trial[i] != pancakes[i])
			{
				match = false;
				break;
			}
		}
	}
	
	printf("Case #%i: %i\n", numCase, answer);
}

int main()
{
	int numCase, cases;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%i", &cases);
	for (numCase = 1; numCase <= cases; numCase++)
		solve(numCase);

	return 0;
}