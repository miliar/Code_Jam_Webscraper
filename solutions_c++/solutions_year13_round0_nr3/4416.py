#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

struct test
{
	int a;
	int b;
};

bool chkPara(int p)
{
	string s = to_string(p);
	int l = s.length();
	for (int i = 0; i < l / 2; ++i)
	{
		if (s[i] != s[l - i - 1]) return false;
	}
	return true;
}

int main()
{
	int t;
	vector<int> vc;
	ifstream fi;
	ofstream fo;
	fi.open("F:\\t\\in");
	fo.open("F:\\t\\out", ios::trunc);
	fi >> t;
	test *ts = new test[t];
	for (int i = 0; i < t; ++i)
		fi >> ts[i].a >> ts[i].b;

	for (int q = 0; q < t; ++q)
	{
		fo << "Case #" << q + 1 << ": ";
		int a = ts[q].a;
		int b = ts[q].b;
		if (q > 0)
		{
			for (int i = 0; i < q; ++i)
			{
				if (a > ts[i].a && a < ts[i].b) a = ts[i].b;
				if (b > ts[i].a && b < ts[i].b) b = ts[i].a;
			}
		}
		for (int i = a; i <= b; ++i)
		{
			if (chkPara(i))
			{
				int k = static_cast<int>(sqrt(i));
				if (k * k == i)
				{
					if (chkPara(k))
					{
						vc.push_back(i);
					}
				}
			}
		}

		int m = 0;
		for (int i = ts[q].a; i <= ts[q].b; ++i)
		{
			for (int j = 0; j < vc.size(); ++j)
			{
				if (i == vc[j])
				{
					++m;
					break;
				}
			}
		}
		fo << m << endl;
	}
	fi.close();
	fo.close();
	return 0;
}