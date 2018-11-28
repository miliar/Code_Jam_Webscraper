#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>
#include <functional>
#include <string>
#include <cmath>

std::ifstream in("input.in");
std::ofstream out("output.txt");

char mine = '*';

typedef std::vector<char> tRow;
typedef std::vector<tRow> tMatrix;

void printMatrix(tMatrix& m, int r, int c)
{
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (m[i][j] == mine)
				out << '*';
			else if (i == 0 && j == 0)
				out << 'c';
			else 
					out << '.';
		}
		out << std::endl;
	}
}

struct data
{
	int n;
	std::vector<std::string> strings;
	long maxLength;
};

void printM(const tMatrix& m, int r, int c)
{
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			std::cout << (int)m[i][j] << " ";
		}
		std::cout << std::endl;
	}
}

void test(data& d)
{
	int n = d.n;
	std::vector<std::string> strings = d.strings;
	long maxLength = d.maxLength;
	//std::cout << "strings =\n ";
	//std::copy(strings.begin(), strings.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
	int totalNum = 0;
	for (int j = 0; ; ++j)
	{
		bool wasOut = false;
		bool wasNotOut = false;
		std::vector<std::string> substrings(n);
		for (int i = 0; i < n; ++i)
		{
			if (strings[i].size() <= j)
			{
				wasOut = true;
				continue;
			}
			else
			{
				wasNotOut = true;
				if (wasOut)
				{
					out << "Fegla Won\n";
					return;
				}
			}
			std::string ch = "";
			ch+= strings[i][j];
			size_t pos = strings[i].find_first_not_of(ch, j);
			substrings[i] = strings[i].substr(j, (pos-j));
			strings[i].replace(j, (pos-j), ch);
		}
	//std::cout << "strings =\n ";
	//std::copy(strings.begin(), strings.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
	//std::cout << "substrings = \n";
	//std::copy(substrings.begin(), substrings.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
		if(wasOut && wasNotOut)
		{
			out << "Fegla Won\n";
			return;
		}

		if (wasOut)
		{
			out << totalNum << "\n";
			return;
		}
		int localMin = 0;
		bool checked = false;
		for (int i = 0; i < n; ++i)
		{
			int m = 0;
			for (int k = 0; k < n; ++k)
			{
				if (!checked)
				{
					if (substrings[i][0] != substrings[k][0])
					{
						out << "Fegla Won\n";
						return;
					}
				}
				int diff = substrings[i].size();
				diff -= (int) substrings[k].size();
				m += fabs((double) diff);
				//std::cout << "m = " << m << std::endl;
			}
			if (!checked)
			{
				checked = true;
				localMin = m;
			}
			else
			{
				localMin = std::min(localMin, m);
			}
		}
		totalNum += localMin;
		//std::cout << "localMin = " << localMin << std::endl;
		//std::cout << "totalNum = " << totalNum << std::endl;
		//std::copy(substrings.begin(), substrings.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
		//return;
	}
}

int main()
{
	int numOfTCs;
	in >> numOfTCs;
	std::vector<data> tests(numOfTCs);
	for (int i = 0; i < numOfTCs; ++i)
	{
		in >> tests[i].n;
		tests[i].strings.resize(tests[i].n);
		tests[i].maxLength = 0;
		for (int s = 0; s < tests[i].n; ++s)
		{
			//std::string str = "";
			//std::getline(in, tests[i].strings[s]);
			in >> tests[i].strings[s];
			//tests[i].maxLength = std::max(tests[i].maxLength, tests[i].strings[s].size());
		}
	}

	for (int i = 1; i <= numOfTCs; ++i)
	{
		out << "Case #" << i << ": ";
		test(tests[i-1]);
	}
}
