#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int judge(string s)
{
	int count = 0;
	char st = s[s.length() - 1];
	if ( st == '-')
		count++;
	for (int i = s.length() - 2; i >= 0; i--)
	{
		if (s[i] != st)
			count++;
		st = s[i];
	}
	return count;
}
int main()
{
	int T;
	string s;
	int t = 0;
	int temp = 0;
	ofstream out;
	out.open("B-large.out", ios::out);
	ifstream in;
	in.open("B-large.in", ios::in);
	in >> T;
	//flag = new int[10];

	while (T > 0)
	{
		T--;
		t++;
		in >> s;
		int j = 0;
		int nu;
		nu = judge(s);
		out << "Case #" << t << ": " << nu << endl;
	}
	in.close();
	out.close();
	return 0;
}