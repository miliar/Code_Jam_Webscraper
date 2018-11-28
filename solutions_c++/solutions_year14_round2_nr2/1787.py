#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

#define FLAG 0

template<class T>
void printVec(const vector<T>& m)
{
	unsigned long l = l = m.size() - 1;
	cout << "Vector: ";
	for (unsigned long i = 0; i < l; ++i)
	{
		cout << m[i] << ", ";
	}
	cout << m[l] << endl;
}

void div(void)
{
	cout << "\n-------------\n";
}

unsigned long work(unsigned long a, unsigned long b, unsigned long k)
{
	unsigned long counter = 0;
	for (unsigned long i = 0; i < a; ++i)
	{
		for (unsigned long j = 0; j < b; ++j)
		{
			if ( (unsigned long)(i&j) < k)
				++counter;
		}
	}
	return counter;
}

int main()
{
	std::ifstream in_file;
	std::ofstream out_file;
	string in_name = FLAG == 0 ? "B-small-attempt0.in" : (FLAG == 1 ? "A-small-practice.in" : "A-large-practice.in"),
		out_name = in_name.substr(0, in_name.length() - 2) + "out";
	cout << in_name << ", " << out_name << "\n\n";

	in_file.open(in_name, ifstream::in);
	if (!in_file.is_open())
	{
		cerr << "Problem opening input file" << endl;
		getchar();
		return 1;
	}
	out_file.open(out_name, ifstream::out);
	if (!in_file.is_open())
	{
		cerr << "Problem opening output file" << endl;
		getchar();
		return 1;
	}

	unsigned long lines;
	in_file >> lines;

	for (unsigned long i = 0; i < lines; ++i)
	{
		//Get variables for the case
		unsigned long a, b, k;
		in_file >> a >> b >> k;
		
		//Actual Work
		unsigned long c = work(a, b, k);

		//Write result to file
		out_file << "Case #" << i + 1 << ": " << c << "\n";
		//cout << "Case #" << i + 1 << ": " << c << "\n";
	}


	in_file.close();
	out_file.close();
	cout << "\n\n-------------\nDone..." << endl;
	getchar();
	return 0;
}
