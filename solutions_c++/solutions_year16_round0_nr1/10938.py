#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;

void add(int x, vector<int>& nums);
string toString(int in);
int toInt(string in1);

int main()
{
	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("result.txt");

	string numTry;
	input >> numTry;

	string N;

	int numTryInt = toInt(numTry);

	for (int i = 0; i < numTryInt; i++)
	{
		//output << i+1;
		vector<int> nums;
		input >> N;
		int initialN = toInt(N);

		if(N == "0")
		{
			//cout << "INSOMNIA" << endl;
			output << " " << "Case #" << i+1 <<": " << "INSOMNIA" << endl;
		}
		else
		{
			int count = 1;
			while(true)
			{
				int Nint = initialN * count;
				N = toString(Nint);
				for (int j = 0; j < N.length(); j++)
				{
					int digit = N[j] - '0';

					add(digit, nums);
				}
				if(nums.size() == 10)
				{
					output << " " << "Case #" << i+1 << ": "  << Nint;
					if(i != (numTryInt -1))
						output << endl;
					break;
				}
				count++;
			}
		}
	}
}

int toInt(string in1)
{
	int ret = atoi(in1.c_str());
	return ret;
}

string toString(int in)
{
	 ostringstream ss;
     ss << in;
     return ss.str();
}

void add(int x, vector<int>& nums)
{
	if(nums.size() == 0)
		nums.push_back(x);
	for (int i = 0; i < nums.size(); i++)
	{
		if(nums[i] == x) 
			break;
		if(i == (nums.size() -1))
			nums.push_back(x);
	}
}