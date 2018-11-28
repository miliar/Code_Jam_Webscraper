//A_Standing Ovation.cpp -- Google Code Jam Qualification Round 2015
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
typedef long long ll;
using namespace std;
const int maxn = 1000 + 10;
char kry[maxn];
int main()
{
//	freopen("in.in", "r", stdin);
//	freopen("out.out", "w", stdout);
	int T, s, ans = 0;
	scanf("%d", &T);
	while( T-- )
	{
		scanf("%d", &s);
		scanf("%s", kry);
		ll cnt = 0, cou = 0;
		for( int i=0; i<s+1; i++ )
		{
			if( i>cnt )
			{
				cou += i-cnt;
				cnt += i-cnt;
			}
			cnt += kry[i]-'0';
		}
		printf("Case #%d: %lld\n", ++ans, cou);
	}
	return 0;
}
