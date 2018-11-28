#include <algorithm>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

// https://mattmccutchen.net/bigint/
#include "bigint-2010.04.30\\BigUnsigned.hh"

using namespace std;

#define IN_FILE "D:\\C-large.in"
#define OUT_FILE "D:\\code_jam_out.txt"

#define MAX 1500

void func(ifstream& in, ofstream& out)
{
    long long N, J;
    in >> N >> J;

    int j = 0;

	string n = "1";

	for (long long i = 0; i < N - 2; i++)
		n += "0";

	n += "1";

	for (int i = 0; i < MAX; i++)
	{
		int div[11];
		int all_good = 1;

		for (int base = 2; base <= 10; base++)
		{
			BigUnsigned cur = 0;
			for (long long i = 0; i < N; i++)
				cur = cur * base + (n[i] - '0');

			int good = 0;
			for (int i = 2; i < MAX; i++)
				if (cur % i == 0)
				{
					good = 1;
					div[base] = i;
					break;
				}

			all_good &= good;
		}

		if (all_good)
		{
			out << n << " ";
			for (int i = 2; i <= 10; i++)
				out << div[i] << " ";
			out << endl;

			j++;
			if (j == J)
				return;
		}

		n[N - 2]++;
		for (int i = N - 2; i >= 0 && n[i] == '2'; i--)
		{
			n[i] = '0';
			n[i - 1]++;
		}
	}
}

int main()
{
	ifstream in;
	in.open(IN_FILE);

	ofstream out;
	out.open (OUT_FILE);
	//out << fixed << showpoint << setprecision(7);

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		//cout << "Case #" << t << endl;
		//out << "Case #" << t << ": ";
		out << "Case #" << t << ":" << endl;
		func(in, out);
	}

	in.close();
	out.close();

	return 0;
}
