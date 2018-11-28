#include <fstream>
#include <iostream>
using namespace std;


int main()
{
	int t;
	cin >> t;

	int k, c, s;

	fstream fout;
	fout.open("d_output.out", ios::out);

	for(int i=1; i<=t; i++)
	{
		cin >> k >> c >> s;

		fout << "Case #" << i << ":";

		for(int j=1; j<=k; j++)
		{
			fout << " " << j;
		}
		fout << endl;
	}

	return 0;
}

