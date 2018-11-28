#include <string>
#include <fstream>
#include <vector>
#include <algorithm>


int GetValue(std::string s, int offset)
{
	int result = 0;
	int numQ = 0;
	for (int i = 0; i < s.size(); i++)
	{
		char c = s[s.size() - i - 1];
		if (c == '?')
		{
			result += (int)pow(10.0, (double)i) * (int)((offset / (int)pow(10.0, (double)numQ)) % 10);
			numQ++;
		}
		else
		{
			result += (int)pow(10.0, (double)i) * (int)(c - 48);
		}
	}
	return result;
}


std::string GetStr(std::string s, int offset)
{
	std::string result;
	result.resize(s.size());
	int numQ = 0;
	for (int i = 0; i < s.size(); i++)
	{
		char c = s[s.size() - i - 1];
		if (c == '?')
		{
			result[s.size() - i - 1] = (char)(48 + ((offset / (int)pow(10.0, (double)numQ)) % 10));
			numQ++;
		}
		else
		{
			result[s.size() - i - 1] = c;
		}
	}
	return result;
}


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	unsigned int numCases = 0;
	in >> numCases;
	for (unsigned int i = 1; i <= numCases; i++)
	{
		out << "Case #" << i << ": ";

		std::string C, J;
		in >> C >> J;

		int cm = 0;
		for each(char c in C)
		{
			if (c == '?')
				cm++;
		}
		cm = (int)pow(10.0, (double)cm);

		int jm = 0;
		for each(char j in J)
		{
			if (j == '?')
				jm++;
		}
		jm = (int)pow(10.0, (double)jm);

		int minDifference = INT_MAX;
		std::string cMin, jMin;

		for (unsigned int c = 0; c < cm; c++)
		{
			int cval = GetValue(C, c);
			for (unsigned int j = 0; j < jm; j++)
			{
				int jval = GetValue(J, j);

				int diff = abs(cval - jval);
				if (diff < minDifference)
				{
					cMin = GetStr(C, c);
					jMin = GetStr(J, j);
					minDifference = diff;
				}
			}
		}

		out << cMin << ' ' << jMin << std::endl;
	}

	return 0;
}


