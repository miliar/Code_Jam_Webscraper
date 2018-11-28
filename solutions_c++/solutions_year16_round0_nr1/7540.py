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
	int count;
	long long input, number, answer, mod, temp;
	bool used[10];
	
	memset(used, 0, 10);
	
	scanf("%lli", &input);
	if (input == 0)
	{
		printf("Case #%i: INSOMNIA\n", numCase);
	}
	else
	{
		number = input;
		count = 0;
		answer = -1;
		while (answer == -1)
		{
			temp = number;
			while (temp > 0)
			{
				mod = temp % 10;
				temp = temp / 10;
				if (!used[mod])
				{
					used[mod] = 1;
					count++;
				}

				if (count == 10)
				{ 
					answer = number;
					break;
				}
					
			}

			number = number + input;
		}
		printf("Case #%i: %i\n", numCase, answer);
	}
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