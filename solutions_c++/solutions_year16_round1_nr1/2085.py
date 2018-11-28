#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

ifstream in;
ofstream out;
int test;
string s;

int main()
{
	in.open("A-large.in");
	out.open("output.txt");

	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		// input
		in >> s;

		string result = "";
		result.push_back(s[0]);
		for (int i = 1; i < s.size(); ++i)
		{
			if (s[i] >= result[0])
				result = s[i] + result;
			else
				result.push_back(s[i]);
		}

		// output
		out << "Case #" << t << ": " << result << endl;
	}

	in.close();
	out.close();
	return 0;
}