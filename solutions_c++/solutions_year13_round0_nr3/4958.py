#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>


inline bool ispalindrome(double n)
{
	int i, j;

	std::string str = std::to_string(n);
	for (i = str.size(); i >= 0 && str[i] != '.'; --i) ;
	str.erase(i);

	for (i = 0, j = str.size() - 1; i < j; ++i, --j)
		if (str[i] != str[j])
			return false;

	return true;
}


int main(int argc, char * argv[])
{
	using namespace std;

	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " inputFile\n";
		exit(EXIT_FAILURE);
	}

	ifstream infile;
	infile.open(argv[1]);
	if (!infile.is_open())
	{
		cerr << "Could not open the file " << argv[1]
			<< "\nProgram terminating.\n";
		exit(EXIT_FAILURE);
	}

	ofstream outfile;
	char * filename = new char[strlen(argv[1]) + 2];
	strcpy(filename, argv[1]);
	strcpy(filename + strlen(argv[1]) - 2, "out");
	outfile.open(filename);

	int n;
	double min, max, i;

	int count;
	infile >> count;
	int * state = new int[count];
	for (n = 0; n < count; ++n)
		state[n] = 0;

	for (n = 0; n < count; ++n)
	{
		infile >> min >> max;

		for (i = ceil(sqrt(min)); pow(i, 2) <= max; ++i)
			if (ispalindrome(i) && ispalindrome(i * i))
				++state[n];
	}

	for (n = 0; n < count; ++n)
		outfile << "Case #" << n + 1 << ": " << state[n] << endl;

	delete [] filename;
	delete [] state;
	outfile.close();
	infile.close();

	return EXIT_SUCCESS;
}
