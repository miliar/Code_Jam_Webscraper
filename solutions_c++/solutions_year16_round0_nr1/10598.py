#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
#include <math.h>

using namespace std;

string solve(long N)
{
	if (N != 0)
	{
		vector<string> str(10);
		str.push_back("0");
		str.push_back("1");
		str.push_back("2");
		str.push_back("3");
		str.push_back("4");
		str.push_back("5");
		str.push_back("6");
		str.push_back("7");
		str.push_back("8");
		str.push_back("9");
		for (long i = 1;; ++i)
		{
			string num = to_string(i*N);
			for (int j = 0; j < str.size(); ++j)
			{
				std::string::size_type index = num.find(str[j]);
				if (index != std::string::npos)
				{
					str.erase(str.begin() + j);
					--j;
				}
			}
			if (str.size() == 0)
				return num;
		}
	}
	return "INSOMNIA";
}
int main()
{
	long T;
	cin >> T;
	for (long i = 1; i <= T; ++i)
	{
		long N;
		cin >> N;
		cout << "Case #" << i << ": " << solve(N) << endl;
	}
	return 0;
}