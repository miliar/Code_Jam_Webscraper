#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>


typedef unsigned __int64 longInt;


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

		longInt N = 0;
		in >> N;

		if (N == 0)
		{
			out << "INSOMNIA" << std::endl;
		}
		else
		{
			longInt i = 1;
			std::set<char> digits;
			while (digits.size() < 10)
			{
				//Add N(i++)'s digits to the digits variable
				longInt X = N * i++;
				std::stringstream c;
				c << X;
				std::string str;
				c >> str;

				for each(char c in str)
				{
					if (digits.find(c) == digits.end())
					{
						digits.insert(c);
					}
				}
			}
			out << N*(i - 1) << std::endl;
		}
	}

	return 0;
}


