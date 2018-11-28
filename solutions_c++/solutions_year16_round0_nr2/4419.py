#include<stdio.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

int T;
string s;

int main()
{
	ifstream in("B-large.in");
	//ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;
	for (int test = 1; test <= T; ++test)
	{
		// input
		in >> s;

		// rough하게, [('-' 덩어리) * 2] 번 만에 가능함.
		// (처음이 '-'로 시작하면 1 감소)
		int len = s.length();
		int result = 0;
		for (int i = 0; i < len; ++i)
		{
			if (s[i] == '-')
			{
				int j = i + 1;
				for (; j < len; ++j)
				{
					if (s[j] == '+')
						break;
				}
				i = j;
				result += 2;
			}
		}
		if (s[0] == '-')
			result--;

		out << "Case #" << test << ": " << result << endl;
	}

	in.close();
	out.close();
	return 0;
}