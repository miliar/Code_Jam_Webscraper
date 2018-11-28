#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <memory.h>
#include <limits.h>
#include <queue>

using namespace std;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s.size() != 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
}

string str[101];
vector <int> a[100];

int main()
{
	prepare("");
	int test;
	cin >> test;
	for (size_t t = 0; t < test; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		int n;
		cin >> n;
		string s;
		getline(cin, s);

		for (size_t i = 0; i < n; i++)
		{
			string temp;
			getline(cin, temp);
			str[i] = temp[0];
			a[i].push_back(1);
			for (size_t j = 1; j < temp.length(); j++)
			{
				if (str[i][str[i].size() - 1] == temp[j])
				{
					a[i][a[i].size() - 1]++;
				}
				else
				{
					str[i] += temp[j];
					a[i].push_back(1);
				}
			}
		}


		int sz = a[0].size();
		bool flag = 1;
		for (size_t i = 1; i < n; i++)
		{
			if (a[i].size() != sz)
			{
				flag = 0;
			}
		}
		if (flag)
		{
			for (size_t i = 0; i < sz; i++)// номер символа
			{
				char chp = str[0][i];
				for (size_t j = 1; j < n; j++)
				{
					if (chp != str[j][i])
					{
						flag = 0;
					}
				}
			}
		}
		if (!flag)
		{
			cout << "Fegla Won\n";
		}
		else
		{
			int res = 0;
			
			int sri[3];
			int resi[3];

			for (size_t i = 0; i < sz; i++)
			{
				int sum = 0;
				for (size_t j = 0; j < n; j++)
				{
					sum += a[j][i];
				}
				sri[0] = abs(sum / n - 1);
				sri[1] = sum / n;
				sri[2] = sum / n + 1;

				resi[0] = 0;
				resi[1] = 0;
				resi[2] = 0;

				for (size_t j = 0; j < n; j++)
				{
					resi[0] += abs(a[j][i] - sri[0]);
					resi[1] += abs(a[j][i] - sri[1]);
					resi[2] += abs(a[j][i] - sri[2]);
				}

				res += min(resi[0], min(resi[1], resi[2]));
			}

			cout << res << endl;

		}
		for (size_t i = 0; i < n; i++)
		{
			a[i].clear();
		}
	}
	return 0;
}
