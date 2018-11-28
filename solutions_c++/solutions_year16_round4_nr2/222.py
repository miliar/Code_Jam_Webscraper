#include <bits/stdc++.h>
using namespace std;

int n , k;
double p[201];

double pro[2][201];

int main()
{
	int test;scanf("%d" , &test);
	for(int t = 1 ; t <= test ; t++)
	{
		scanf("%d%d" , &n , &k);
		for(int i = 0 ; i < n ; i++)scanf("%lf" , &p[i]);
		sort(p , p + n);
		double ans = 0;
		for(int pre = 0 ; pre <= k ; pre++)
		{
			int ind = 0;
			for(int i = 0 ; i <= k ; i++)pro[0][i] = 0;
			pro[0][0] = 1;

			for(int j = 0 ; j <= pre + 0 - 1 ; j++)
			{
				ind ^= 1;
				for(int i = 0 ; i <= k ; i++)
					pro[ind][i] = 0;
				for(int i = 0 ; i < k ; i++)
					pro[ind][i + 1] += pro[ind ^ 1][i] * p[j];
				for(int i = 0 ; i <= k ; i++)
					pro[ind][i] += pro[ind ^ 1][i] * (1 - p[j]);
			}
			for(int j = n - 1 ; j >= (n - k + pre) ; j--)
			{
				ind ^= 1;
				for(int i = 0 ; i <= k ; i++)
					pro[ind][i] = 0;
				for(int i = 0 ; i < k ; i++)
					pro[ind][i + 1] += pro[ind ^ 1][i] * p[j];
				for(int i = 0 ; i <= k ; i++)
					pro[ind][i] += pro[ind ^ 1][i] * (1 - p[j]);
			}
			
			if(pro[ind][k / 2] > ans)
				ans = pro[ind][k / 2];

		}
		printf("Case #%d: %.10f\n" , t , ans);
	}
	return 0;
}