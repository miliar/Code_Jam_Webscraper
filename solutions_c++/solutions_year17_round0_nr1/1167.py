#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
string s;
int k;
bool done;

int main()
{
	ifstream in("A-large.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> s >> k;
		int n = (int)s.size();
		
		int cnt = 0;
		for (int i = 0; i <= n - k; ++i)
		{
			if (s[i] == '+')
				continue;

			for (int j = i; j < i + k; ++j)
			{
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			cnt++;
		}
		
		bool flag = true;
		for (int i = 0; i < n; ++i)
		{
			if (s[i] == '-')
				flag = false;
		}

		if (flag)
			out << "Case #" << t << ": " << cnt << endl;
		else
			out << "Case #" << t << ": IMPOSSIBLE" << endl;
	}

	in.close();
	out.close();
	return 0;
}