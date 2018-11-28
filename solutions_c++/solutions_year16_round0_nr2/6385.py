#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<vector>
using namespace std;
bool allplus(string st);

int main()
{
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	//cout<<"T: "<<T<<endl;
	long long int num;

	for (int t = 1; t <= T; t++)
	{
		string st;
		cin >> st;
		int count = 0;
		while (!(allplus(st)))
		{
			if (st[0] == '+')
			{
				int i = 0;
				while (st[i] == '+')
				{
					st[i] = '-';
					i++;
				}
				count++;
			}
			else if (st[0] == '-')
			{
				int i = 0;
				while (st[i] == '-')
				{
					st[i] = '+';
					i++;
				}
				count++;
			}
		}

		cout << "Case #" << t << ": ";
		cout << count << endl;

	}
//	system("pause");
//	return 0;
	exit(0);
}

bool allplus(string st)
{
	for (int i = 0; i < st.length(); i++)
	{
		if (st[i] == '-')
			return false;
	}
	return true;
}
