#include <iostream>
#include <string>
#include <assert.h>
#include <fstream>

using namespace std;

int main()

{
	fstream myfile, output;
	cout << "enterfilename" << endl;
	string filename;
	cin >> filename;
	myfile.open(filename, ios::in);
	output.open("output.txt", ios::out);
	int t, n; // t  = test cases , n current line entry.
	myfile >> t;
	bool *w = new bool[10];
	bool solved = false;
	int temp;
	string x;
	assert(t >= 1 && t <= 100);
	for (int i = 0; i < t; i++)
	{
		myfile >> n;
		for (int i = 0; i < 10; i++)
		{
			w[i] = false;
		}
		solved = false;
		assert(n >= 0 && n <= pow(10,6));
		if (n == 0) {
			output << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
		else
		{
			int count = 0;
			while (!solved)
			{
				count++;
				temp = n * (count);
				x = to_string(temp);
				for (int j = 0; j < x.size(); j++)
				{
					if (!w[x[j] - '0'])
					{
						w[x[j]-'0'] = true;
						int z = 0;
						while (w[z])
						{
							z++;
							if (z == 10)
							{
								solved = true;
								break;
							}
						}
					}
					if (solved) break;
				}
			}
			output << "Case #" << i+1 << ": " << temp << endl;
		}
	}
	myfile.close();
	output.close();


}