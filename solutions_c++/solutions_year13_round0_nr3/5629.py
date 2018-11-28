#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
#include <list>
#include <cmath>

using namespace std;

typedef string (*solve_Tpf)(ifstream &);

void usage(char *programName)
{
	cerr << programName << " [inputfile]" << endl;
	exit(-1);
}

bool isPalindrome(int i)
{
	ostringstream o;
	o << i;
	string str = o.str();
	if (str.length() == 1)
		return true;

	int length = str.length();
	for(int i = 0 ; i < length / 2 + (length % 2 == 0 ? 0 : 1) ; i++)
	{
		if (str[i] != str[length - 1 - i])
			return false;
	}

	return true;
}

string count(ifstream & i)
{
	string result;
	int count = 0;
	if (i)
	{
		string line;
		getline(i, line);
		istringstream in(line);
		getline(in, line, ' ');
		long start = atol(line.c_str());
		getline(in, line);
		long end = atol(line.c_str());
		time_t startingTime = time(0);
		for(long s = sqrt(start) ; s <= sqrt(end) ; s++)
		{
			if (isPalindrome(s))
			{
				long square = s * s;

				if (square >= start && isPalindrome(square))
					++count;
			}
		}
	}
	ostringstream out;
	out << count;
	return out.str();
}
void resolve(char *filename, solve_Tpf func)
{
	if (func == 0)
		return;

	ifstream i(filename);

	if (i)
	{
		int index;
		string line;
		getline(i, line);
		int testcases = atoi(line.c_str());

		for(index = 1 ; index <= testcases ; ++index)
		{
			cout << "Case #" << index << ": " << func(i) << endl;
		}

		i.close();
	}
}

int main(int argc, char **argv)
{
	if (argc != 2)
		usage(argv[0]);

	//storeCredit(argv[1]);
	//time_t startingTime = time(0);
	resolve(argv[1], &count);
	//cout << "Execute en " << (time(0) - startingTime) << endl;

	return EXIT_SUCCESS;
}
