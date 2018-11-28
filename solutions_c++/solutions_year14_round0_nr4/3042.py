#include <cstdio>
#include <algorithm>
using namespace std;
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int p = 0; p < t; ++p)
	{
		int n;
		scanf ("%d", &n);
		double a[n], b[n];
		for (int i = 0; i < n; ++i)
			scanf ("%lf", &a[i]);
		for (int j = 0; j < n; ++j)
			scanf ("%lf", &b[j]);
		int f1[1001], f2[1001];
		int kk = -99;
		double x = 2.0;
		for (int i = 0; i < 1000; ++i)
			f1[i] = f2[i] = -99;
		int c1 = 0, c2 = 0; 
		sort (a, a + n);
		sort (b, b + n);
		for (int j = 0; j < n; ++j)
		{
			kk = -99;
			x = 2.0;
			for (int i = 0; i < n; ++i)
			{
				if (a[j] - b[i] < x && (a[j] - b[i] > 0) && f1[i] == -99)
				{
					x = a[j] - b[i];
					kk = i;	
				}	
			}
			if (kk != -99 && f1[kk] == -99)
				f1[kk] = j;		
		}
		for (int i = 0; i < n; ++i)
			if (f1[i] != -99)
				++c1;
		for (int j = 0; j < n; ++j)
		{
			kk = -99;
			x = 2.0;
			for (int i = 0; i < n; ++i)
			{
				if ((b[j] - a[i] < x) && (b[j] - a[i] > 0) && (f2[i] == -99))
				{
					x = b[j] - a[i];
					kk = i;	
				}	
			}
			if (kk != -99 && f2[kk] == -99)
				f2[kk] = j;
		}
		for (int i = 0; i < n; ++i)
			if (f2[i] != -99)
				++c2;
		printf ("Case #%d: %d %d\n", p+1, c1, n-c2);			
	}	
	return 0;
}