#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define INF mod
#define pi acos(-1.0)
#define LINF 1000000000000000000LL
#define eps 1e-10

//A
/*
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		ll i;
		int mask = 0;
		for(i = n; ; i += n)
		{
			ll k = i;
			while(k)
			{
				mask |= (1 << (k % 10));
				k /= 10;
			}
			if(mask == 1023)
				break;
		}
		printf("Case #%d: %lld\n", t, i);
	}
	return 0;
}
*/

//B
/*
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		int cnt = 0;
		while(1)
		{
			bool ok = true;
			for(int i = 0; i < s.size(); i++)
				if(s[i] == '-')
					ok = false;
			if(ok)
				break;
			int i;
			for(i = s.size() - 1; i >= 0; i--)
				if(s[i] == '-')
					break;
			if(s[0] == '+')
			{
				cnt++;
				for(int j = 0; j < s.size() && s[j] == '+'; j++)
					s[j] = '-';
			}
			cnt++;
			for(int j = 0; j <= i; j++)
				s[j] = (s[j] == '+' ? '-' : '+');
			for(int j = 0; j < i - j; j++)
				swap(s[j], s[i-j]);
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
*/

//D
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		ll k, c, s;
		cin >> k >> c >> s;
		printf("Case #%d:", t);
		ll step = 1;
		for(int i = 0; i < c - 1; i++)
			step *= k;
		for(ll i = 1; i <= step * k; i += step)
			printf(" %lld", i);
		puts("");
	}
	return 0;
}