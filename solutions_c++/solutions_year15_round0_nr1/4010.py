#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream inpFile;
	ofstream outFile;
	inpFile.open("A-large.in");
	outFile.open("output.out3");

	int T;
	inpFile >> T;
	for (int j = 0; j < T; ++j)
	{
		int n;
		string str;
		inpFile >> n >> str;

		int standing = (int)str[0]-48, needed=0;

		for (int i = 1; i <= n; ++i)
		{
			if(i > standing && (int)str[i] -48 > 0)
			{
				needed += (i-standing);
				standing += (i-standing)+((int)str[i] -48);
			}
			else
			{
				standing += (int)str[i]-48;
			}
		}

		outFile << "Case #" << j+1 << ": " << needed << endl;
	}
	

	return 0;
}