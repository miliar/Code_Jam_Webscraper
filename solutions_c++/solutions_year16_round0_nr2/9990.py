#include<algorithm>
#include<vector>
#include<math.h>
#include <iostream>
#include<stdio.h>
#include <iomanip>
#include <fstream>
#include<string>

using namespace std;

int main()
{
	ifstream inf("input.in");
	ofstream outf("output.out");

	//-- check if the files were opened successfully 
	if (!inf.is_open()) cout << "input.in was not open successfully" << endl;
	if (!outf.is_open()) cout << "output.out was not open successfully" << endl;

	int t;
	inf >> t;
	for (int i = 0; i < t; i++)
	{
		string signes;
		inf >> signes;
		int counter = 1;

		for (int i = 1; i < signes.size(); i++){
			if (signes[i] != signes[i - 1])
				counter++;
		}
		if (signes[0] == '-'&&signes[signes.length() - 1] == '-')
		{
				outf << "Case #" << i + 1 << ": " << counter<< endl;
		}
		else if (signes[0] == '-'&&signes[signes.length() - 1] == '+')
		{
			outf << "Case #" << i + 1 << ": " << counter - 1 << endl;
		}
		else if (signes[0] == '+'&&signes[signes.length() - 1] == '-')
		{
			outf << "Case #" << i + 1 << ": " << counter << endl;
		}
		else if (signes[0] == '+'&&signes[signes.length() - 1] == '+')
		{
			outf << "Case #" << i + 1 << ": " << counter-1 << endl;
		}
	}
	inf.close();
	outf.close();

	system("pause");
	return 0;
}
