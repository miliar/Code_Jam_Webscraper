#include<stdio.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

bool IsDone();

int T;
long long int n;
bool digit[10];
string s;

int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");

	in >> T;
	for (int test = 1; test <= T; ++test)
	{
		// init
		for (int i = 0; i < 10; ++i)
			digit[i] = false;

		// input
		in >> n;

		out << "Case #" << test << ": ";

		if (n == 0)
		{
			out << "INSOMNIA" << endl;
			continue;
		}

		// process
		long long int result = n;
		long long int max = (long long int)pow(10, 17);
		for (long long int i = n; i <= max; i += n)
		{
			s = to_string(i);
			int len = s.length();
			for (int p = 0; p < len; ++p)
				digit[s[p] - '0'] = true;

			result = i;
			if (IsDone())
				break;
		}
		out << result << endl;
	}

	in.close();
	out.close();
	return 0;
}

bool IsDone()
{
	for (int i = 0; i < 10; ++i)
	{
		if (digit[i] == false)
			return false;
	}
	return true;
}