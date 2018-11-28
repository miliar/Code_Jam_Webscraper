#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

int used;
const int check = 1023;

bool findDigits(long long num)
{
	do {
		int digit = num % 10;

		used |= (1 << digit);

		if (used == check)
			return true;

		num /= 10;
	} while (num > 0);

	return false;
}

int main()
{
	fstream in("in.in"), out("out.txt");

	srand(time(NULL));

	int T;

	in >> T;

	string tt;
	getline(in, tt, '\n');

	for (int t = 1; t <= T; ++t)
	{
		string s;
		vector<char> stack;
		int res;

		getline(in, s, '\n');

		stack.push_back(s[0]);

		for (int i = 1; i < s.length(); ++i)
		{
			if (s[i] == '-' && stack.back() != '-')
				stack.push_back(s[i]);
			else if (s[i] == '+' && stack.back() != '+')
				stack.push_back(s[i]);
		}

		if (stack.size() == 1)
		{
			if (stack.front() == '+')
				res = 0;
			else
				res = 1;
		}
		else if (stack.size() % 2 == 0)
		{
			if (stack.front() == '+')
				res = stack.size();
			else
				res = stack.size() - 1;
		}
		else
		{
			if (stack.front() == '+')
				res = stack.size() - 1;
			else
				res = stack.size();
		}

		out << "Case #" << t << ": " << res << endl;
	}

	in.close();
	out.close();

	return 0;
}