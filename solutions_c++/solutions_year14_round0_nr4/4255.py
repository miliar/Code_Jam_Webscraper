#include <iostream>
#include <algorithm>
using namespace std;

double va[1000], vb[1000];

void print(double *begin, double *end)
{
	double *iter;
	for (iter = begin; iter != end; iter++)
		cout << *iter << ' ';
	cout << endl;
}

void solve()
{
	int n, i, j, del, count;
	bool ok;
	
	cin >> n;
	for (i = 0; i < n; i++)
		cin >> va[i];
	for (i = 0; i < n; i++)
		cin >> vb[i];
	
	sort(va, va + n);
	sort(vb, vb + n);
	
	//print(va, va + n);
	//print(vb, vb + n);
	
	for (del = 0; !ok; del++)
	{
		ok = true;
		for (i = del; i < n; i++)
			if (va[i] < vb[i-del])
			{
				ok = false;
				break;
			}
		if (ok) cout << n - del << ' ';
	}
	
	j = count = 0;
	for (i = 0; i < n; i++)
	{
		while (va[i] > vb[j])
		{
			j++;
			if (j == n) break;
		}
		if (j < n) count++; else break;
		j++;
	}
	cout << n - count << endl;
}

int main()
{
	int t, i;
	
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	
	return 0;
}