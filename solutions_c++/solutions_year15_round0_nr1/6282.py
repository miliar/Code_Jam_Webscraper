#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	int num_cases = 0;
	int case_size = 0;
	int num_chars = 0;
	char string[1002];
	int people_needed = 0;
	int people_standing = 0;
	int total_people_needed = 0;

	//ifstream ifs("a-large.in");
	//ifs >> num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; i++)
	{
		//ifs >> num_chars;
		cin >> num_chars;
		num_chars++;
		cin >> string;
		// do algorithm
		for (int j = 0; j < num_chars; j++)
		{
			int value = (int)(string[j] - '0');

			if (value != 0 &&
				people_standing < j)
			{
				people_needed = j - people_standing;
				people_standing += people_needed;
				total_people_needed += people_needed;
			}

			people_standing += value;
			people_needed = 0;
		}

		cout << "Case #" << i + 1 << ": " << total_people_needed << endl;

		// reset variables
		memset(&num_chars, 0, sizeof(int));
		memset(string, 0, sizeof(char) * 1002);
		people_needed = 0;
		people_standing = 0;
		total_people_needed = 0;
	}
	return 0;
}