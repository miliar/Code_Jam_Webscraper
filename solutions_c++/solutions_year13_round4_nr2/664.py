#include<cstdio>
#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	//init();
	
	//printf("Input File Name ?");
	char FileName[128];
	//scanf("%s", FileName);
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	int Case;
	for(Case = 1;  Case <= T; Case ++)
	{
		__int64 n, m, p, q;
		scanf("%I64d %I64d", &n, &m);
		
		__int64 S = (1LL<<n);
		__int64 ans1 = 0;
		p = S/2; q = 2;
		__int64 sum = p;
		
		if(m == S)
		{
			ans1 = S-1;
		}
		else {
			while(m > sum)
			{
				p /= 2;
				sum += p;
				ans1 += q;
				q *= 2;
			}
		}
		
		__int64 ans2 = S-1;
		p = S; q = 1;
		while(m < p)
		{
			p /= 2;
			ans2 -= q;
			q *= 2;
		}
		
		printf("Case #%d: %I64d %I64d\n", Case, ans1, ans2);
	}
	
	return 0;
}
