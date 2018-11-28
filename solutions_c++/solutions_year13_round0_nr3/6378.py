#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

void FindLimits(string line, int* lower, int* upper)
{
	int space = line.find(' ');

	*lower = atoi(line.substr(0, space).c_str());
	*upper = atoi(line.substr(space + 1).c_str());
}

bool IsPalindrome(int number)
{
	stringstream ss; ss << number;
	string temp = ss.str();
	bool palin = true;

	for (int i = 0; i < temp.length(); ++i)
	{
		if (temp[i] == temp[temp.length() - i - 1])
			palin = true;
		else
			return false;
	}

	return palin;
}

int main()
{
	ifstream in_file("C-small-attempt0.in");
	ofstream out_file("out_file.txt");
	int test_cases = 0;

	string temp = "";
	getline(in_file, temp);
	test_cases = atoi(temp.c_str());

	for (int current_case = 0; current_case < test_cases; ++current_case)
	{
		int lower = 0, upper = 1;

		string line = "";
		getline(in_file, line);
		FindLimits(line, &lower, &upper);

		int counter = 0;
		for (int i = lower; i <= upper; ++i)
		{
			/*stringstream ss; ss << i;
			string str = ss.str();*/
			/*if (str.length() == 2 || str.length() == 4 || str.length() == 8 || str.length() == 10 || str.length() == 14)
				continue;
			if (str.back() != '1' || str.back() != '4' || str.back() != '5' || str.back() != '6' || str.back() != '9')
				continue;*/
			float root = sqrt((float)i);
			int i_root = root;
			if (root == i_root)
				if (IsPalindrome(i) && IsPalindrome((int)root))
					++counter;
		}

		out_file << "Case #" << current_case + 1 << ": " << counter << endl;
	}

	out_file.close();
	in_file.close();

	cin.get();
	return 0;
}