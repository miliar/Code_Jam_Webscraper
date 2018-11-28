#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	int t;
	int k;
	int c;
	int s;

	long k_part;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> k >> c >> s;

		k_part = 1;
		for (int i = 1; i < c; i++)
		{
			k_part *= k;
		}

		output << "Case #" << run << ":";

		if (c == 1)
		{
			if (s < k)
			{
				output << " IMPOSSIBLE";
			}
			else
			{
				for (int i = 1; i <= k; i++)
				{
					output << " " << i;
				}
			}
		}
		else if (2*s < k)
		{
			output << " IMPOSSIBLE";
		}
		else
		{
			for (int i = 0; i < k - 1; i += 2)
			{
				output << " " << i*k_part + i + 2;
			}

			if (k % 2 == 1)
			{
				output << " " << k*k_part;
			}
		}

		output << "\n";
//		cout << run << "\n";
	}

	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
