#include <iostream>
#include <new>
//#include <cstring>
#include <utility>
#include <string>
#include <list>
#include <unordered_map>

using namespace std;
/*
char plus_cov[5] = { '0', '1', 'i', 'j', 'k' };
char minus_cov[5] = { '0', '1', 'x', 'y', 'z' };
int map[5][5] = { 
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2, -1, 4, -3 },
	{ 0, 3, -4, -1, 2 },
	{ 0, 4, 3, -2, -1 },
};

char mlt(char s, char t)
{

	return map[i][j];
}
*/
int main(void)
{
	int t;
	int i;

	/*make map*/
	unordered_map<string, unordered_map<string, string >> tbl;

	tbl["1"]["1"] = "1";
	tbl["1"]["i"] = "i";
	tbl["1"]["j"] = "j";
	tbl["1"]["k"] = "k";
	tbl["i"]["1"] = "i";
	tbl["i"]["i"] = "-1";
	tbl["i"]["j"] = "k";
	tbl["i"]["k"] = "-j";
	tbl["j"]["1"] = "j";
	tbl["j"]["i"] = "-k";
	tbl["j"]["j"] = "-1";
	tbl["j"]["k"] = "i";
	tbl["k"]["1"] = "k";
	tbl["k"]["i"] = "j";
	tbl["k"]["j"] = "-i";
	tbl["k"]["k"] = "-1";

	tbl["-1"]["-1"] = "1";
	tbl["-1"]["-i"] = "i";
	tbl["-1"]["-j"] = "j";
	tbl["-1"]["-k"] = "k";
	tbl["-i"]["-1"] = "i";
	tbl["-i"]["-i"] = "-1";
	tbl["-i"]["-j"] = "k";
	tbl["-i"]["-k"] = "-j";
	tbl["-j"]["-1"] = "j";
	tbl["-j"]["-i"] = "-k";
	tbl["-j"]["-j"] = "-1";
	tbl["-j"]["-k"] = "i";
	tbl["-k"]["-1"] = "k";
	tbl["-k"]["-i"] = "j";
	tbl["-k"]["-j"] = "-i";
	tbl["-k"]["-k"] = "-1";

	tbl["-1"]["1"] = "-1";
	tbl["-1"]["i"] = "-i";
	tbl["-1"]["j"] = "-j";
	tbl["-1"]["k"] = "-k";
	tbl["-i"]["1"] = "-i";
	tbl["-i"]["i"] = "1";
	tbl["-i"]["j"] = "-k";
	tbl["-i"]["k"] = "j";
	tbl["-j"]["1"] = "-j";
	tbl["-j"]["i"] = "k";
	tbl["-j"]["j"] = "1";
	tbl["-j"]["k"] = "-i";
	tbl["-k"]["1"] = "-k";
	tbl["-k"]["i"] = "-j";
	tbl["-k"]["j"] = "i";
	tbl["-k"]["k"] = "1";

	tbl["1"]["-1"] = "-1";
	tbl["1"]["-i"] = "-i";
	tbl["1"]["-j"] = "-j";
	tbl["1"]["-k"] = "-k";
	tbl["i"]["-1"] = "-i";
	tbl["i"]["-i"] = "1";
	tbl["i"]["-j"] = "-k";
	tbl["i"]["-k"] = "j";
	tbl["j"]["-1"] = "-j";
	tbl["j"]["-i"] = "k";
	tbl["j"]["-j"] = "1";
	tbl["j"]["-k"] = "-i";
	tbl["k"]["-1"] = "-k";
	tbl["k"]["-i"] = "-j";
	tbl["k"]["-j"] = "i";
	tbl["k"]["-k"] = "1";

	cin >> t;

	for (i = 0; i < t; i++)
	{
		int l, m;

		cin >> l;
		cin >> m;

		char * tok = new char[l + 1];
		char * str = new char[l*m + 1];

		cin >> tok;

		int j;

		strcpy(str, tok);
		for (j = 1; j < m; j++)
		{
			strncat(str, tok, l);
		}

		/*****************main algorithm*****************************************/
		list<string> test, ypos, kpos;
		string ans;
		ans = "NO";

		for (j = 0; j < l*m; j++)
		{
			string tmp;
			tmp = str[j];
			test.push_back(tmp);
		}

		string a, b;

		a = test.front();
		test.pop_front();

		while (!test.empty())
		{
			if (a == "i")
			{
				a = test.front();
				test.pop_front();

				ypos = test;
				while (!test.empty())
				{
					if (a == "j")
					{
						a = test.front();
						test.pop_front();

						kpos = test;

						while (!test.empty())
						{
							b = test.front();
							test.pop_front();
							a = tbl[a][b];
						}

						if (a == "k")
						{
							ans = "YES";
						}
					}
					else
					{
						b = test.front();
						test.pop_front();
						a = tbl[a][b];
					}
				}
			}
			else
			{
				b = test.front();
				test.pop_front();
				a = tbl[a][b];
			}
		}

		/************************************************************************/
		cout << "Case #" << i + 1 << ": " << ans << endl;

		delete[] tok;
		delete[] str;
	}

	return 0;
}
