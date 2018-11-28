#include <iostream>
#include <set>
#include <string>
#include <cmath>
using namespace std;

typedef unsigned long long ull;

int main()
{
	ull x;
	cin >> x;
	for (ull i = 0; i < x; i++)
	{
		int k, c, s;
		cin >> k >> c >> s;
		std::cout << "Case #" << i + 1 << ": ";
		for (int i = 0; i < s; i++)
		{
			std::cout << i * (ull) pow(k, c - 1) + 1 << " ";
		}
		std::cout << std::endl;
	}
}