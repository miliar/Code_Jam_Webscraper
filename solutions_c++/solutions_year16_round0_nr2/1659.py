#include <iostream>
#include <string>

using namespace std;

int solve(const string& pancakes)
{
	int flips = 0;
	for (int k = 1; k < pancakes.size(); k++)
	{
		flips += (pancakes[k] != pancakes[k - 1]);
	}
	flips += pancakes.back() == '-';
	return flips;
}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; c++)
	{
		string pancakes;
		cin >> pancakes;
		printf("Case #%d: %d\n", c, solve(pancakes));
	}
	return 0;
}