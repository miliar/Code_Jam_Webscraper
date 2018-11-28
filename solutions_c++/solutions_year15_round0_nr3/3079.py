#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

ifstream in("C1.in");
ofstream out("C1.out");

string mul(char a, char b)
{
	if (a == '1')
	{
		return string(1, b);
	}

	if (a == 'i')
	{
		if (b == '1') return "i";
		if (b == 'i') return "-1";
		if (b == 'j') return "k";
		if (b == 'k') return "-j";
	}

	if (a == 'j')
	{
		if (b == '1') return "j";
		if (b == 'i') return "-k";
		if (b == 'j') return "-1";
		if (b == 'k') return "i";
	}

	if (a == 'k')
	{
		if (b == '1') return "k";
		if (b == 'i') return "j";
		if (b == 'j') return "-i";
		if (b == 'k') return "-1";
	}

	return "error";
}

string mul(const string& a, const string& b)
{
	int minusA = 1;
	if (a[0] == '-')
		minusA = -1;

	int minusB = 1;
	if (b[0] == '-')
		minusB = -1;

	string c = mul(a.back(), b.back());
	int znak = minusA * minusB;
	if (c[0] == '-')
		znak *= -1;

	if (znak == -1)
		return string("-") + c.back();
	return string(1, c.back());
}

int main()
{
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		int L, x;
		string tmp, s;
		in >> L >> x >> tmp;
		for (int i = 0; i < x; ++i)
			s = s + tmp;

		string answer = "NO";

		//cout << s << endl;
		string st(1, s[0]);
		for (int i = 1; i < s.size(); ++i)
		{
			st = mul(st, string(1, s[i]));
			//cout << "mul = " << st << endl;
		}
		cout << "Step1" << endl;
		string skizb = "1";
		if (st == "-1")
		for (int i = 0; i < s.size(); ++i)
		{
			skizb = mul(skizb, string(1, s[i]));
			//cout << "skizb = " << skizb << endl;
			if (skizb == "i")
			{
				string verj = "1";
				for (int j = s.size() - 1; j > i; --j)
				{
					verj = mul(string(1, s[j]), verj);
					if (verj == "k")
					{
						answer = "YES";
						goto kl;
					}
				}
			}
		}

	kl:

		out << "Case #" << t << ": " << answer << endl;
	}
}