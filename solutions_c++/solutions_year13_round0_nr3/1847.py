#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

char str[55];

vector<long long> pre;

long long gen1(long long a)
{
	long long ret = a;
	while(a > 0)
	{
		ret = ret * 10 + (a % 10);
		a /= 10;
	}
	return ret;
}

long long gen2(long long a)
{
	long long ret = a;
	a /= 10;
	while(a > 0)
	{
		ret = ret * 10 + (a % 10);
		a /= 10;
	}
	return ret;
}

bool ispalin(long long x)
{
	sprintf(str, "%lld", x);
	int i, j, len;
	len = strlen(str);
	for(i = 0, j = len - 1; i < j; i++, j--)
	{
		if(str[i] != str[j])
			return false;
	}
	return true;
}

long long getind(long long a)
{
	long long ret;
	for(ret = 0; ret < pre.size(); ret++)
	{
		if(pre[ret] > a)
		{
			return(ret - 1);
		}
	}
	return(ret);
}

int main()
{
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	freopen("C-large-1.in", "rt", stdin);
	freopen("C-large-1.out", "wt", stdout);

	long long inp, kase, i, j, k;
	long long a, b;
	for(i = 1; i < 10000; i++)
	{
		long long pl = gen1(i);
		long long pl2 = pl * pl;
		if(ispalin(pl2))
		{
			pre.push_back(pl2);
		}
		pl = gen2(i);
		pl2 = pl * pl;
		if(ispalin(pl2))
		{
			pre.push_back(pl2);
		}
	}
	sort(pre.begin(), pre.end());
	scanf("%lld", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%lld %lld", &a, &b);
		i = getind(a);
		j = getind(b);
		if(i >= 0 && pre[i] == a)
		{
			i--;
		}
		printf("Case #%lld: %lld\n", kase, j - i);
	}

	return 0;
}