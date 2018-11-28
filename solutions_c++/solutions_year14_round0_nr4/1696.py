#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

using namespace std;
const int X = 1010;
double lst1[X], lst2[X];
set <double> st;
double eps = 1e-6;
bool used[X];
int main()
{
	int i, j, n, m, test, cnt_test, cnt, a1, a2, z = 0;
	double x, c, f, time = 0, v = 2.0;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cnt_test;
	cout.precision(20);
	cout << fixed;
	for(test = 1; test <= cnt_test; test++)
	{
		cin >> n;
		m = 0;
		a1 = 0; a2 = 0;
		for(i = 0; i < n; i++) cin >> lst1[i];
		for(i = 0; i < n; i++) cin >> lst2[i];
		sort(lst1, lst1 + n);
		sort(lst2, lst2 + n);
		for(i = 0; i < X; i++)
		{
			used[i] = false;
		}
		a2 = n;
		j = n-1;
		i =n-1;
		for(j = n - 1, i = n - 1; j > -1 && i >-1; i--)
		{
			//cerr << i << ' ' << j;
			if(used[i])  break;
			while(j > -1 && lst1[j] > lst2[i])
			{
				used[m++] = true;
				j--;
			}
			if(j > -1 && !used[i]) a2--, j--; 
		}
		z = n - 1;
		for(j = 0, i = 0; j < n && i <= z; j++)
		{
			if(lst1[j] > lst2[i]) 
			{
				a1++;
				i++;
			}
			else
			{
				z--;
			}
		}
		cout <<"Case #" << test  << ": " << a1 << " " << a2 <<  '\n';
	}
	return 0;
}