#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

#if 0
istream& in = cin;
ostream& out = cout;
#else
istream& in = ifstream("in");
ostream& out = ofstream("out");
#endif

int main()
{
	int C, level;
	string num_str;

	in >> C;

	for (int c = 1; c <= C; c++)
	{
		in >> level;
		in >> num_str;

		vector<int> nums;
		for (auto i = 0L; i < num_str.size(); i++)
			nums.push_back(num_str[i] - '0');

		int count = 0;
		int need = 0;

		count += nums[0];
		for (auto i = 1U; i <= level; i++)
		{
			int gap = count - i;
			if (gap < 0)
			{
				need -= gap;
				count -= gap;
			}
			count += nums[i];
		}

		out << "Case #" << c << ": " << need << endl;
	}

	return 0;
}
