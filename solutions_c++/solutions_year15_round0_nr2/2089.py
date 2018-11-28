#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n,k;
	cin >> k;
	vector<long long> x;
	long long m=0, s, a,p;
	for (int i = 1; i <= k; i++)
	{
		cin >> n;
		x = vector<long long>(n);
		for (int j = 0; j < n; j++)
		{
			cin >> x[j];
			m = max(m, x[j]);
		}
		p  = m;
		
		for (int j = 1; j <= m; j++)
		{
			s = j;
			for (int z = 0; z < n; z++)
			{
				s += x[z] / j;
				if (x[z] % j != 0) s++;
				s--;
			}
			if (s < p) p = s;
		}
		cout << "Case #" << i << ": " << p << endl;;
	}
	return 0;
}
