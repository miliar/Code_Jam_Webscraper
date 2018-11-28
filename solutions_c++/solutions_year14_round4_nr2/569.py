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

int solve(vector<int> v)
{
	int res = 0;
	while(v.size())
	{
		int n = v.size();
		int id = 0;
		for(int i = 0; i < n; i++)
			if(v[i] < v[id])
				id = i;
		res += min(id, n-id-1);
		v.erase(v.begin()+id);
	}

	return res;
}

int brut(vector<int> v)
{
	int n = v.size();
	int res = 1<<30;
		for(int id = 0; id < n; id++)
		{
			vector<int> q(v);
			int cur = 0;
			for(int i = 0; i < v.size(); i++)
			{
				for(int j = 0; j+1 < id; j++)
				{
					if(q[j] > q[j+1])
					{
						swap(q[j], q[j+1]);
						cur++;
					}
				}
			}

			for(int i = 0; i < v.size(); i++)
			{
				for(int j = id; j+1 < v.size(); j++)
				{
					if(q[j] < q[j+1])
					{
						swap(q[j], q[j+1]);
						cur++;
					}
				}
			}
			res = min(res, cur);
		}
	return res;

}

vector<int> test()
{
	int n = rand()%10+1;
	set<int> res;
	while(res.size() < n)
		res.insert(rand());
	vector<int> ret(res.begin(), res.end());
	random_shuffle(ret.begin(), ret.end());
	return ret;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	/*while(true)
	{
		vector<int> v = test();
		if(solve(v) != brut(v))
		{
			puts("!!!");
			return 0;
		}
		else
			putchar('.');
	}*/

	int t = nextint();
	for(int test = 1; test <= t; test++)
	{
		int n = nextint();
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			v[i] = nextint();
		


		//printf("Case #%d: %d\n", test, brut(v));
		printf("Case #%d: %d\n", test, solve(v));
	}

	return 0;
}