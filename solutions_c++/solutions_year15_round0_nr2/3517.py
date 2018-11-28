#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>

#define inf 1000000000

using namespace std;

long long n, m, s, t, ans = 0,k;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output2.txt");
	long long mx,mi = inf, s;
	long long t;
	cin>>t;
	for (int tt = 0; tt < t; tt++)
	{
		mi = inf;
		mx = -1;
		vector <long long> a;
		a.clear();
		long long d,size;
		cin >> size;
		for (int love = 0; love < size; love++)
		{
			long long buf;
			cin >> buf;
			a.push_back(buf);
		}
		for (int love = 0; love < a.size(); love++)
			mx = max(mx, a[love]);
		for (int j = 1; j <=mx; j++)
		{
			s = j;
			for (int k = 0; k < size; k++)
			{
				if (a[k] > j)
				{
					if (a[k] % j == 0)
						s += a[k] / j - 1;
					else
						s += a[k] / j;
				}
			}
			mi = min(s, mi);
		}
		cout << "Case #" << tt + 1 << ": " << mi << endl;
	}
	//system("pause");
}