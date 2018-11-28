#include<iostream>
#include<iomanip>
#include<memory.h>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cs;
	cin >> cs;
	for (int tc = 1; tc <= cs; tc++)
	{
		int n,sc0,sc1;
		sc0 = sc1 = 0;
		double a[1000], b[1000];
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		int ph = 0, pt = n - 1;
		for (int i = n-1; i >=0; i--)
		{
			if (a[i]>b[pt])
			{
				sc0++;
				ph++;
			}
			else
			{
				pt--;
			}
		}
		ph = 0;
		for (int i = 0; i < n; i++)
		{
			while (ph < n)
			{
				if (a[ph] < b[i])
					ph++;
				else
				{
					sc1++;
					ph++;
					break;
				}
			}
		}
		cout << "Case #" << tc << ": " << sc1 << ' ' << sc0 << endl;
	}
	return 0;
}