#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
ll func(int c, int base)
{
	if(base == 2) return c;
	ll ret = 0;
	ll c2 = 1;
	for(int i = 0; i < 16; i++)
	{
		if(((c >> i) & 1) != 0) ret += c2;
		c2 *= base;
	}
	return ret;
}
int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t, n, j2;
	scanf("%d", &t);
	scanf("%d %d", &n, &j2);
	printf("Case #1:\n");
	int c = 32769;
	int c2;
	int c3 = 0;
	for(int i = 0; i < 16384 && c3 < 50; i++)
	{
		c2 = c | (i<<1);
		vector<ll> r2;
		for(int j = 2; j <= 10; j++)
		{
			ll val = func(c2, j);
			bool b = false;
			for(ll k = 2; k * k <= val; k++)
			{
				if(val % k == 0)
				{
					r2.push_back(k);
					b = true;
					break;
				}
			}
			if(!b)
			{
				r2.clear();
				break;
			}
		}
		if(!r2.empty())
		{
			for(int j = 15; j >= 0; j--)
			{
				if(((c2 >> j) & 1) != 0) printf("1");
				else printf("0");
			}
			for(int i = 0; i < r2.size(); i++) printf(" %I64d", r2[i]);
			printf("\n");
			c3++;
		}
	}
	return 0;
}
