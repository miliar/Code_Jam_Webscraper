/*
  Beautiful Codes are MUCH better than 'Shorter' ones !
user  : triveni
date  : 10/04/2016
time  : 00:33:01
*/
#include <bits/stdc++.h>

using namespace std;

#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           make_pair(a,b)
#define      pb(a)             push_back(a)
#define      each(it,s)        for(auto it = s.begin(); it != s.end(); ++it)
#define      rep(i, n)         for(int i = 0; i < (n); ++i)
#define      fill(a)           memset(a, 0, sizeof (a))
#define      sortA(v)          sort(v.begin(), v.end())
#define      sortD(v)          sort(v.begin(), v.end(), greater<auto>())
#define      X                 first
#define      Y                 second

typedef long long LL;
LL MOD = 1000000007;

int main()
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		printf("Case #%d: ",tc);
		int n;
		cin >> n;
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		int mask = 0, val = 0, finalMask = (1<<10)-1;
		for(int i = 0; i < 10000 && mask < finalMask; ++i) {
			val += n;
			int val1 = val;
			while(val1 > 0) {
				int d = val1 % 10;
				val1 /= 10;
				mask = (mask |(1<<d));
			}
		}
		assert(mask == finalMask);
		printf("%d\n",val);
	}
	return 0;
}
