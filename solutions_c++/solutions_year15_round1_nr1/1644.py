#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int data[10005];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T, index=1;
	cin >> T;
	while (T--)
	{
		cout << "Case #" << index++ << ": ";
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)cin >> data[i];
		int s1 = 0, s2 = 0;
		for (int i = 1; i < n; ++i)
		{
			if (data[i] < data[i - 1])s1 += (data[i - 1] - data[i]);
		}
		bool valid = true;
		for (int i = 1; i < n; ++i)
		{
			valid = valid && (data[i] >= data[i - 1]);
		}
		if (valid == true)s2 = 0;
		else
		{
			double r = 0;
			for (int i = 0; i < n - 1; ++i)
			{
				if (data[i] > data[i + 1])
				{
					r = max(r, (data[i] - data[i + 1]) / 10.0);
				}
			}
			for (int i = 0; i < n - 1; ++i)
				s2 += min((int)(r * 10), data[i]);
		}
		
		cout << s1 << " " << s2 << endl;
	}
	return 0;
}