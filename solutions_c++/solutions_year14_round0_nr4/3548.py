#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <set>
using namespace std;

int main()
{
	freopen("D-small-attempt0.in.txt", "r", stdin);
	freopen("ou.txt", "w", stdout);	
	int T; scanf("%d", &T);
	for (int ii=0; ii<T; ii++)
	{
		int n; scanf("%d", &n);
		vector<double>a = vector<double>();
		vector<double>b = vector<double>();
		set<double> set2 = set<double>();
		
		for (int i=0; i<n; i++) 
		{
			double f; scanf("%lf", &f);
			a.push_back(f);
		}
		
		for (int i=0; i<n; i++) {
			double f; scanf("%lf", &f);
			b.push_back(f);
			set2.insert(f);
		}
		
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		
		// for (int i=0; i<n; i++)
		// 	printf("%lf ", a[i]);
		// printf("\n");
		// 
		// for (int i=0; i<n; i++)
		// 	printf("%lf ", b[i]);
		// printf("\n");
		
		int s = 0; int bh = 0; int bt = n-1;
		for (int i=0; i<n; i++)
		{
			if (a[i] > b[bh])
			{
				s ++;
				bh++;
			}
			else
			{
				bt --;
			}
		}
		
		int s1 = 0;
		for (int i=0; i<n; i++)
		{
			set<double>::iterator it = set2.upper_bound(a[i]);
			if (it == set2.end())
			{
				s1 ++;
				set2.erase(set2.begin());
			}
			else
			{
				set2.erase(it);
			}
		}
		printf("Case #%d: %d %d\n", ii+1, s, s1);
	}
	
	return 0;
}