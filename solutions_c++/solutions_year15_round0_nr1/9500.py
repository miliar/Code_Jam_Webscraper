#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

bool isPossible(vector<int> audience, int value)
{
	vector<int> partSums(audience.size(), 0);
	partSums[0] = audience[0] + value;
	for (int i = 1; i < partSums.size(); i++)
		partSums[i] = audience[i] + partSums[i-1];
	
	for (int i = partSums.size() - 1; i >= 0; i--)
		if (i >= partSums[i])
			return false;

	return true;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " input_file" << endl;
		return 1;
	}

	string line, number;
	ofstream outfile;
	ifstream infile;
	int test, noTests, maxShyness, result;
	bool ok = false;

	outfile.open("Output.out");
	infile.open(argv[1]);

	if (infile.is_open())
	{
		getline(infile, line);
		noTests = atoi(line.c_str());

		for (test = 1; test <= noTests; test++)
		{		
			getline(infile, line);
			stringstream stream(line);

			stream >> maxShyness;

			vector<int> audience(maxShyness + 1, 0);
			vector<int> partSums(maxShyness + 1, 0);
			stream >> number;
			
			for(int i = 0; i < number.size(); i++)
				audience[i] = number[i] - '0';

			for(result = 0; result <= maxShyness; result++)
				if (isPossible(audience, result))
					break;

			outfile << "Case #" << test << ": " << result << endl;
		}
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file";

	return 0;
}