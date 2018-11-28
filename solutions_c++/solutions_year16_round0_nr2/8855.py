#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>

using namespace std;

void sw(string &s,int q)
{
	for (int i = q; i >= 0; i--)
	{
		if (s[i] == '-')
		{
			s[i] = '+';
		}
		else
			s[i] = '-';
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
/*
	cout << 1000001 << endl;
	for (long long i = 0; i < 1000001; i++)
		cout << i << endl;
	return 0;*/
	long long t;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		string s;
		cin >> s;
		long long ans = 0;
		for (int q = s.size() - 1; q >= 0; q--)
		{
			if (s[q] == '-')
			{
				sw(s,q);
				ans++;
			}
		}


		cout << "Case #" << i + 1 << ": ";


		cout << ans << endl;

	}



	return 0;
}