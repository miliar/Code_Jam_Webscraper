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

	int ans;
	int t;
	string s;

	char k;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> s;
		ans = 0;

		k = s[0];
		for (char c : s)
		{
			if (k != c)
			{
				ans++;
				k = c;
			}
		}

		if (k == '-')
		{
			ans++;
		}

		output << "Case #" << run << ": " << ans << "\n";
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
