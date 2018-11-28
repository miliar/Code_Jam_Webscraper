#include<cstdio>
#include<iostream>
using namespace std;
const int MAX_ALPHA = 30;

int a[MAX_ALPHA];

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		int n;
		cin >> n;
		int len = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			len += a[i];
		}
		cout << "Case #" << (q + 1) << ": ";
		int pos = 0;
		int ost = len;
		if (len % 2 != 0)
		{
			ost--;
			for (int i = 0; i < n; i++)
				if (a[i] > a[pos])
					pos = i;
			cout << (char)(pos + 'A') << " ";
			a[pos]--;
		}
		while (ost > 0)
		{
			pos = 0;
			for (int i = 0; i < n; i++)
				if (a[i] > a[pos])
					pos = i;
			cout << (char)(pos + 'A');
			a[pos]--;
			int pos2 = 0;
			if (pos == 0)
				pos2++;
			for (int i = 0; i < n; i++)
				if (a[i] > a[pos2] && i != pos)
					pos2 = i;
			cout << (char)(pos2 + 'A') << " ";
			a[pos2]--;
			ost -= 2;
		}
		cout << "\n";
	}
	return 0;
}