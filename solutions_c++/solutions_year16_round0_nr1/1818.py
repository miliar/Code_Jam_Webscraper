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
	int n;

	bool digits_seen[10];
	int num_of_digits_seen;
	string current;
	int current_digit;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> n;
		ans = 0;

		if (n == 0)
		{
			output << "Case #" << run << ": " << "INSOMNIA" << "\n";
			continue;
		}

		for (int i = 0; i < 10; i++)
		{
			digits_seen[i] = false;
		}
		num_of_digits_seen = 0;

		while (true)
		{
			ans += n;
			current = to_string(ans);
			for (char c : current)
			{
				current_digit = c - '0';
				if (!digits_seen[current_digit])
				{
					digits_seen[current_digit] = true;
					num_of_digits_seen++;
				}
			}

			if (num_of_digits_seen == 10)
			{
				break;
			}
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
