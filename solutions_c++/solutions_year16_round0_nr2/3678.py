#include <iostream>
#include<algorithm>
#include<string>
#include<map>
#include<fstream>
using namespace std;

bool arr[10];

int main()
{
	ifstream inf;
	inf.open("B-large.in", std::ifstream::in);
	ofstream outf;
	outf.open("out.txt", std::ofstream::out);
	int t; inf >> t;
	for (int i = 1; i <= t; i++)
	{
		string s; inf >> s;
		int cnt = 0; int a = s.length()-1;
		if (s.length() == 1)
		{
			if (s[0] == '+')cnt = 0;
			else cnt = 1;
		}
		else {
			while (a >= 0 && s[a] == '+')
				a--;
			for (a; a >= 0; a--)
				if (s[a] != s[a + 1])cnt++;
		}
		outf << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}
