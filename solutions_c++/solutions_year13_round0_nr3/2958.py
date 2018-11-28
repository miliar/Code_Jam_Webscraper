#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

void init();
bool isPal(long long num);

vector<long long> v;
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	init();
	for (int t=1; t<=cas; t++)
	{
		long long a, b;
		scanf("%lld %lld", &a, &b);
		int posa = 0, posb = v.size();
		for (int i=0; i<v.size()-1; i++)
		{
			if (v[i]<a && v[i+1]>=a)
			{
				posa = i + 1;
				break;
			}
		}
		for (int i=v.size()-1; i>0; i--)
		{
			if (v[i-1]<=b && v[i]>b)
			{
				posb = i - 1;
				break;
			}
		}
		printf("Case #%d: %d\n", t, (posb-posa+1));
	}
	return 0;
}

void init()
{
	long long num = 1;
	while (num <= 10000000)
	{
		if (isPal(num) && isPal(num*num))
		{
			v.push_back(num*num);
			//printf("%lld\n", num*num);
		}
		num++;
	}
}

bool isPal(long long num)
{
	char s[105];
	int pos = 0;
	while (num > 0)
	{
		s[pos++] = num%10 + '0';
		num /= 10;
	}
	for (int i=0; i<(pos>>1); i++)
	{
		if (s[i] != s[pos-i-1])
			return false;
	}
	return true;
}