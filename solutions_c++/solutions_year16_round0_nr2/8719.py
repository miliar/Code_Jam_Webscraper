#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;

	in.open("B-large.in");
	out.open("B-large.txt");

	int cnt = 1, TestCase;

	in >> TestCase;

	while (TestCase--)
	{
		int ret = 0;
		string str;
		in >> str;

		int loop = str.length();
		bool change = false;
		for (int a = str.length() - 1; a >= 0; a--)
		{
			if (str[a] == '+') continue;
			else
			{
				for (int b = 0; b <= a; b++)
				{
					if (str[b] == '+') str[b] = '-';
					else str[b] = '+';
				}
				ret++;

			}
		}
		cout << "Case #" << cnt << ": " << ret << endl;
		out << "Case #" << cnt++ << ": " << ret << endl;
	}
	out.close();
	in.close();
	system("pause");

	return 0;
}