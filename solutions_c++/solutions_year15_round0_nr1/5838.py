#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs)
	{
		unsigned n;
		cin >> n;
		vector<unsigned> shyness(n + 1);
		for (auto& x : shyness)
		{
			char c;
			cin >> c;
			x = unsigned(c - '0');
		}

		size_t currentStanding = shyness[0];
		size_t needed = 0;
		for (size_t i = 1; i < shyness.size(); ++i)
		{
			if (currentStanding < i)
			{
				needed += i - currentStanding;
				currentStanding = i + shyness[i];
			}
			else currentStanding += shyness[i];
		}

		cout << "Case #" << cs << ": " << needed << "\n";
	}

	return 0;
}