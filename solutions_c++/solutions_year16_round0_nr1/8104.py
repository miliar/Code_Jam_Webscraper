#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int a = 0;
	int T = 0;
	vector<int> vec;

	ifstream infile ("A-large.in");
	if (infile.is_open())
	{
		infile >> T; // reads first line.
		
		while (infile >> a) // starting from second line.
		{
			vec.push_back(a); 
		}
	infile.close();
	}

	vector<int> result; // initialize result vector

	
	// iterase through vector
	for (int i=0; i < T; i++)
	{
		int x = vec[i];
		bool digit[10] = {0}; // initialize boolean array to false.
		int tally = 0; // whether all digits have been seen. =10 
		int nx = 0; // keep final number
		
		if (!x)
		{
			result.push_back(0);
			continue;
		}

		while (tally < 10)
		{
			nx += x; // increment nx.
			int temp = nx;			
			int rem; // keep track of last digit.

			while (temp)
			{
				rem = temp%10;
				temp /= 10;
				
				if (!digit[rem])
				{
					digit[rem] = true;
					tally++;	
				}
			}
		}
		result.push_back(nx);	
	}

	ofstream outfile ("q1large.txt");
	
	if(outfile.is_open())
	{
		for (size_t i=0; i < result.size(); ++i)
		{
			if (!result[i])
			{
				outfile << "Case #" << i+1 << ":" << " INSOMNIA\n";
			}
			else {
				outfile << "Case #" << i+1 << ": " << result[i] << endl; 
			}
			
		}
		outfile.close();
		
	}
	
	return 0;
}
	