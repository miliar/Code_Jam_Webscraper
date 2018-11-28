#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int t, i, k, n, res1, res2, p, q, x, y;
	vector<double> a, b; 
	double temp;
	scanf("%d", &t);
	for(k=1; k<=t; k++)
	{
		res1=res2=0;
		scanf("%d", &n);
		for(i=0; i<n; i++)
		{
			scanf("%lf", &temp);
			a.push_back(temp);
		}
		for(i=0; i<n; i++)
		{
			scanf("%lf", &temp);
			b.push_back(temp);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		p=q=n-1;
		for(i=0; i<n; i++)
		{
			if(a[p] > b[q])
			{
				p--;	
				q--;
				res1++;
			}
			else
				q--;
		}
		
		p=q=n-1;
		for(i=0; i<n; i++)
		{
			if(a[p] > b[q])
			{
				p--;
				res2++;
			}
			else
			{
				p--;
				q--;
			}
		}
		
		printf("Case #%d: %d %d\n", k, res1, res2);
		a.clear();
		b.clear();
	}
	return 0;
}
