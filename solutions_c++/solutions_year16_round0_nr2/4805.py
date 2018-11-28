#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
string s;
int main()
{
	ifstream in("B-large.in");
	ofstream out("1.txt");
	int T, i, j, len, num;
	bool flag;
	in >> T;
	getline(in, s);
	for (i = 0; i < T; i++)
	{
		s.clear();
		num = 0;
		getline(in, s);
		len = s.length();
		out << "Case #" << i + 1 << ": ";
		if (s[0] == '-')
			flag = false;
		else
			flag = true;
		for (j = 1; j < len; j++)
		{
			if (s[j] == '-'&&s[j - 1] == '+')
			{
				num += 2;
				flag = true;
			}
			if (s[j] == '+'&&s[j - 1] == '-')
			{
				if(!flag)
					num++;
			}
		}
		if (num == 0 && s[0] == '-')
			num++;
		out << num << endl;
	}
}