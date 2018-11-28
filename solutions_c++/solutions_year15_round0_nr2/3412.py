#include <bits/stdc++.h>
using namespace std;

int test, d;
int a[1100000], b[1100000];
int s;

void upheap(int i)
{
	int j, x;
	j = i/2;
	x = a[i];
		while(j > 0 && a[j] < x)
		{
			a[i] = a[j];
			i = j; j = i/2;
		}
	a[i] = x;
}

void downheap(int i)
{
	int j, x;
	j = i*2;
	x = a[i];
		while(j <= d)
		{
			if(j < d && a[j] < a[j+1]) j++;
			if(x >= a[j]) break;
			a[i] = a[j];
			i = j; j = i*2;
		}
	a[i] = x;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> d;
		for(int i = 0; i < d; i++)
			cin >> a[i];
		int k;
		s = 100000000;
		for(int x = 1; x <= 1000; x++)
		{	
			k = 0;
			for(int i = 0; i < d; i++)
				k += max(0, (a[i] - 1)/x);
			s = min(s, k + x);
		}
		cout << s << "\n";
	}
	return 0;
}