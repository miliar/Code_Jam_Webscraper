#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-small.in");
	ofstream fout("A_small.out");

	int cases;
	fin >> cases;

	for (int i=0; i<cases; ++i)
	{
		unsigned long long radius, paint;
		fin >> radius >> paint;

		unsigned long long count = 0;
		unsigned long long paintNeeded = 2 * radius + 1;
		while (paint >= paintNeeded)
		{
			++count;
			paint -= paintNeeded;
			paintNeeded += 4;
		}

		fout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}