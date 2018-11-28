#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int s[10000];

int main()
{

	ifstream cin ("A-large.in");
	ofstream cout ("out.txt");
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int n, x;
		cin >> n >> x;

		for (int j = 0; j < n; j++)
			cin >> s[j];

		int ats = n;

		sort(s, s+n);

		int l = 0, r = n-1;

		while (l < r)
		{
			if (s[l] + s[r] <= x)
			{
				ats--;
				l++;
				r--;
			} else
				r--;
		}

		cout << "Case #" << i + 1 << ": " << ats << endl;
	}
	
	//while (true) {}
}