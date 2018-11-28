//#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<cmath>
#include<climits>
#include<list>
#include<utility>
#include<memory>
#include<cstddef>
#include<iterator>
#include<iomanip>

using namespace std;
typedef long long LL;
typedef long double LD;
const double pai = acos(-1.0);
///////////////////////////////
int flag[200];
long long n;

long long comp(long long x)
{
	int sum = 0;
	long long m = 0, i, p;

	while (sum < 10)
	{
		char s[100];
		int res = 0;
		m += x;
		p = m;
		while (p != 0)
		{
			s[res++] = p % 10;
			p /= 10;
		}
		for (i = 0; i < res; i++)
		{
			if (!flag[s[i]])
			{
				sum++;
				flag[s[i]] = 1;
			}
		}
	}
	return m;
}
///////////////////////////////
int main(int argc, char**argv) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	////////////////////////////

	int t, count = 0;
	scanf("%d", &t);
	while (t--)
	{
		int i, ans = 0;

		scanf("%lld", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ++count);
			continue;
		}
		memset(flag, 0, sizeof(flag));
		ans = comp(n);
		printf("Case #%d: %d\n", ++count, ans);
	}









	////////////////////////////
	//system("pause");
	return 0;
}

//END

