#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <numeric>
#include <ctime>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <stack>
#include <string>
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
char nextchar(){char a[8];scanf("%s",a);return a[0];}
int nextint(){int a;scanf("%d",&a);return a;}
ll nextll(){ll a;scanf("%lld",&a);return a;}
double nextdouble(){double a;scanf("%lf",&a);return a;}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t = nextint();
	for(int test = 1; test <= t; test++)
	{
		int n = nextint();
		int k = nextint();
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			v[i] = nextint();
		sort(v.rbegin(), v.rend());

		int res = 0;
		for(int i = 0; i < v.size(); i++)
		{
			if(i+1 < v.size())
			{
				if(v[i]+v.back() <= k)
				{
					res++;
					v.pop_back();
				}
				else
				{
					res++;
				}
			}
			else
				res++;
		}
		printf("Case #%d: %d\n", test, res);
	}

	return 0;
}