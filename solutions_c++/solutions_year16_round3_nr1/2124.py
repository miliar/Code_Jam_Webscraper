#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

long long a[27];

int main(){
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+", stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		int n;
		string s="";
		cin >> n;
		for (int i = 0; i < 27; i++)
		{
			a[i] = 0;
		}
		int maxd = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			if (a[i]>maxd)
			{
				maxd = a[i];
			}
		}
		cout << "Case #" << tt << ": ";
		while (maxd > 0)
		{
			for (int i = 0; i < n; i++)
			{
				if (a[i] == maxd)
				{
					s+=(char)(i + (int)'A');
					a[i]--;
					break;
				}
			}
			maxd = 0;
			for (int i = 0; i < n; i++)
			{
				if (a[i]>maxd)
				{
					maxd = a[i];
				}
			}
			if (maxd == 0)
			{
				continue;
			}
			for (int i = 0; i < n; i++)
			{
				if (a[i] == maxd)
				{
					s+=(char)(i + (int)'A');
					a[i]--;
					break;
				}
			}
			maxd = 0;
			for (int i = 0; i < n; i++)
			{
				if (a[i]>maxd)
				{
					maxd = a[i];
				}
			}
		}
		if (s.length() % 2 == 0)
		{
			for (int i = 0; i < s.length(); i += 2)
			{
				cout << s[i] << s[i + 1] << " ";
			}
		}
		else
		{
			cout << s[s.length() - 1] << " ";
			for (int i = 0; i < s.length() - 1; i += 2)
			{
				cout << s[i] << s[i + 1] << " ";
			}
		}
		cout << endl;
	}
	return 0;
}

