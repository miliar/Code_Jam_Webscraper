#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	string line;
	ifstream myfile ("test.txt");
	ofstream ofile;
	int numOfTestCases = 0;
	int chosen = -1;
	vector<int> numbers;
	vector<int> results;
	ofile.open("result.txt");
	if (myfile.is_open())
	{
		getline(myfile, line);
		numOfTestCases = atoi(line.c_str());
		for(int i = 0; i < numOfTestCases; i++)
		{
			getline(myfile, line);
			chosen = atoi(line.c_str());
			for(int j = 0; j < chosen - 1; j++)
			{
				getline(myfile, line);
			}
			getline(myfile, line);
			std::istringstream is( line );
			int n;
			while( is >> n ) {
				numbers.push_back(n);
				// do something with n
			}
			for(int j = 0; j < 4 - chosen; j++)
			{
				getline(myfile, line);
			}

			getline(myfile, line);
			chosen = atoi(line.c_str());
			for(int j = 0; j < chosen - 1; j++)
			{
				getline(myfile, line);
			}
			getline(myfile, line);
			std::istringstream is1( line );
			while( is1 >> n ) {
				for(int t = 0; t < numbers.size(); t++)
				{
					if(numbers[t] == n)
					{
						results.push_back(n);
					}
				}
				// do something with n
			}
			for(int j = 0; j < 4 - chosen; j++)
			{
				getline(myfile, line);
			}
			if(results.size() == 1)
			{
				ofile << "Case #" << i + 1 << ": " << results[0];
			} 
			else if(results.size() > 1)
			{
				ofile << "Case #" << i + 1 << ": Bad magician!";
			}
			else if(results.size() == 0)
			{
				ofile << "Case #" << i + 1 << ": Volunteer cheated!";
			}
			ofile << endl;
			results.clear();
			numbers.clear();
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
	ofile.close();
	return 0;
}


