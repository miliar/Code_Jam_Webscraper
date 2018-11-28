#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

struct numo
{
	double value;
	bool naomi;
};

/*vector<char> getType(string s)
{
	vector<char> result;
	int count;
	result.push_back(s[0]);
	for(int i = 1; i < s.length; i++)
	{
		if(s[i] != result.back)
		{
			result.push_back(s[i]);
		}
		else
	}
	return result;
}*/


int main()
{
	string line, a, b;
	ifstream myfile ("test.txt");
	ofstream ofile;
	int numOfTestCases = 0;
	int n;
	int result = 0;
	vector<vector<char>> table;
	ofile.open("result.txt");
	ofile.precision(7);
	ofile.setf( std::ios::fixed, std:: ios::floatfield );
	if (myfile.is_open())
	{
		getline(myfile, line);
		numOfTestCases = atoi(line.c_str());
		for(int i = 0; i < numOfTestCases; i++)
		{	
			getline(myfile, line);
			n = atoi(line.c_str());
			getline(myfile, a);
			getline(myfile, b);
			if(a.length() < b.length())
			{
				string temp = b;
				b = a;
				a = temp;
			}
			if(a[0] != b[0])
			{
				result = -1;
			}
			int k = 1;
			if(result != -1)
			{
				for(int j = 1; j < a.length(); j++, k++)
				{
					if(a[j] != b[k])
					{
						if(a[j] == a[j-1])
						{
							result++;
							k--;
						}
						else if (b[k] == b[k-1])
						{
							result++;
							j--;
						}
						else
						{
							result = -1;
							break;
						}
					}
				}
			}
			
			if(result == -1)
			{
				ofile << "Case #" << i + 1 << ": Fegla Won" << endl;
			}
			else
			{
				if(k != b.length())
					result += (b.length() - k);
				ofile << "Case #" << i + 1 << ": " << result << endl;
			}
			result = 0;
			ofile << endl;
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
	ofile.close();
	return 0;
}


