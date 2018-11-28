#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ifstream input;
	input.open("A-large.in");
	int TCN;
	input >> TCN;

	ofstream output;
	output.open("output2.out");


	for (int i = 0; i < TCN; i++)
	{
		int maxSn;
		input >> maxSn;
		
		int* audiance = new int[maxSn + 1];
		
		string s;
		input >> s;

		for (int j = 0; j < s.size(); j++)
		{
			audiance[j] = s[j] - '0';
		}

		long long int TotalStanding = 0;
		long long int TotalNeeded = 0;
		for (int j = 0; j <= maxSn; j++)
		{
			if (TotalStanding >= j || audiance[j] == 0)
			{
				TotalStanding += audiance[j];
			}
			else
			{
				TotalNeeded += j - TotalStanding;
				TotalStanding = j + audiance[j];
			}
		}
		output << "Case #" << i + 1 << ": " <<TotalNeeded<< endl;
		delete [] audiance;
	}
}