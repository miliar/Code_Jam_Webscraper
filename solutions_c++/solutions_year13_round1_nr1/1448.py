#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<deque>
#include<queue>
#include<map>
using namespace std;

typedef long long int L;
typedef unsigned long long int U;

main()
{
	int tc;
	cin>>tc;
	for(int x= 1;x<=tc;x++)
	{
		U r,t;
		scanf("%llu %llu", &r, &t);
		U p = (r+1)*(r+1) - r*r;
		int c = 0;
		while(t >= p)
		{
			c++;
			t = t - p;
			p = (r+2*c+1)*(r+2*c+1) - (r+2*c)*(r+2*c);
		}
		printf("Case #%d: %d\n", x, c);
	}
}
