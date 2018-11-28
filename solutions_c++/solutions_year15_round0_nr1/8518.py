#include<iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


int main()
{


	int * cases;

	vector<int> state;
	int standing;
	ifstream infile("A-large.in");
	int a, b;
	string line;

	infile >> a;
	cases = new int[a];
	for (int j = 0; j < a; ++j)
	{
		standing = 0;

		infile >> b >> line;
		if (b == 0)
		{
			cases[j] = 0;
			//cout << "case: " << j + 1 << ": ";
			//cout << "OK" << endl;
			continue;
		}
		//cout << b << " " <<line  << endl;
		int c = line.size();
		for (int k = 0; k < c; ++k)
		{
			string a;
			a[0] = line[k];
			state.push_back(atoi(a.c_str()));

		}

		for (int k = 0; k < c; ++k)
		{
			if (standing >= k)
			{
				standing += state[k];
			}
		}

		if (standing >= b)
		{
			cases[j] = 0;
			//cout << "case: " << j + 1 << ": ";
			//cout << "OK" << endl;

		}
		else
		{

			bool flag = false;
			for (int r = 1; r <= b; ++r)
			{
				
				for (int m = 0; m < c; ++m)
				{
					standing = 0;
					int temp = state[m];
					
					state[m] += r;
					for (int k = 0; k < c; ++k)
					{
						if (standing >= k)
						{
							standing += state[k];
						}
						else
						{
							break;
						}
					}

					if (standing >= b)
					{
						cases[j] = r;
						//cout << "case: " << j + 1 << ": " << r << endl;

						flag = true;
						break;

					}
					state[m] = temp;
				}
				if (flag)
				{
					break;
				}

			}

		}
		state.clear();
	}




	ofstream myfile;
	myfile.open("output.txt");
	for (unsigned k = 0; k < a; ++k)
	{
		myfile << "Case #" << k + 1 << ": " << cases[k] << "\n";
	}

	myfile.close();

	system("PAUSE");
	return 0;
}