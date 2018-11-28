#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (void)
{
	string input;
	int totalApplauding;
	int totalInvites;
	int T;
	int S_max;
	ifstream fin("A-large.in");
	ofstream fout("Output.txt", ios::trunc);
//	cout << "Enter the number of trials: ";
	fin >> T;
//	cout << T << endl;
	for (int Case = 1; Case <= T; Case++)
	{
		fin >> S_max;
		fin >> input;

//		for (int i = 0; i < input.length(); i ++)
//		{
//			cout << (int)input.at(i) - '0' << endl;
//		}

		totalApplauding = 0;
		totalInvites = 0;
//		cout << endl << S_max;
		for (int k = 0; k <= S_max; k ++)
		{
			if (k > totalApplauding)
			{
				totalInvites += (k - totalApplauding);
				totalApplauding = k;
			}
			totalApplauding += (int)input.at(k) - '0';
		}
//		cout << endl;
//		cout << "Case #" << Case << ": " << totalInvites << endl;
		fout << "Case #" << Case << ": " << totalInvites << endl;
	}

	return (0);
}