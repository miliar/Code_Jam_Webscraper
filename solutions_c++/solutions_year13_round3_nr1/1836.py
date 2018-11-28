#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool isVowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'u' || c == 'o';
}

void main()
{
	cout << "input > ";
	string filename;
	cin >> filename;

	ifstream infile(filename.c_str());
	ofstream outfile("a.out");

	uint64_t T;
	infile >> T;

	for (uint64_t t = 1; t<= T; ++t)
	{
		std::string name;
		std::size_t n;
		infile >> name >> n;
		std::size_t nv = 0;

		std::size_t start = 0;
		std::size_t end = n;
		while (start + n <= name.size())
		{
			uint64_t numConsonants = 0;

			for (std::size_t i = start; i < end; ++i)
			{
				if (!isVowel(name[i]))
					++numConsonants;
				else
					numConsonants = 0;
				
				if (numConsonants == n)
				{
					++nv;
					break;
				}
			}

			++end;
			if (end > name.size())
			{
				++start;
				end = start + n;
			}
			
		}

		outfile << "Case #" << t << ": " << nv << std::endl;
	}
}
