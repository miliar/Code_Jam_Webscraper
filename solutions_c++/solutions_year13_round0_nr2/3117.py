#include <iostream>
#include <algorithm>
#include "stdio.h"


using namespace std;


int n, m;



int main()
{
	int t;
	cin >> t;
	
	for(int CASE = 1; CASE <= t; CASE ++)
	{
		int a[201][201];
		scanf("%d %d", &n, &m);
		int i, j;

		for(i = 0; i < n; i ++)
		{
			for(j = 0; j < m; j ++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		int lx = 0;
		int ly = 0;
		int largest = a[0][0];
		for(i = 0; i < n; i ++)
		{
			for(j = 0; j < m; j ++)
			{
				if(a[i][j] > largest)
				{
					largest = a[i][j];
					lx = i; ly = j;
				}
			}
		}
		
		bool possible = true;
		for(i = 0; i < n; i ++)
		{
			for(j = 0; j < m; j ++)
			{
				if(i == lx || j == ly)
					continue;
				int t1 = a[lx][j];
				int t2 = a[i][ly];
				int tt;
				if(t1 < t2)
					tt = t1;
				else tt = t2;
				if(a[i][j] != tt)
				{
					possible = false;
					break;
				}
			}
			if(!possible)
				break;
		}
		if(possible)
			printf("Case #%d: YES\n", CASE);
		else
			printf("Case #%d: NO\n", CASE);
	}
	return 0;
	
}