/*
	Author:USETC_elfness
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<map>
typedef long long LL;
const int V=100100;
const int P=1000000007;
using namespace std;
int n, m;
LL cnt[V], tmp[V], ret[V], s[V];
map<LL, int> mp;
int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for(int ca = 1; ca <= _; ++ca)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
		scanf("%lld", &s[i]);
		for(int i = 0; i < n; ++i)
		scanf("%lld", &cnt[i]);
		LL S = 0;
		for(int i = 0; i < n; ++i) S += cnt[i];
		mp.clear();
		for(int i = 0; i < n; ++i) mp[s[i]] = i;
		m = 0;
		for(int i = 1; ; ++i)
		if((1LL << i) == S) {m = i; break;}
		for(int i = 0; i < m; ++i)
		{
			for(int j = 0; j < n; ++j)
			if(cnt[j] > 0)
			{
                if(s[j] == 0)
                {
                    bool can = true;
                    for(int k = 0; k < n; ++k)
                    if(cnt[k] % 2 != 0) {can = false;break;}
                    if(can)
                    {
                        for(int k = 0; k < n; ++k) cnt[k] /= 2;
                        ret[i] = 0;
                        break;
                    }
                    continue;
                }
				LL df = max(s[j], -s[j]);
				int id = -1;
				bool can = true;
				for(int k = 0; k < n; ++k) tmp[k] = cnt[k];
				for(int k = n - 1; k >= 0; --k)
				{
				    if(tmp[k] == 0) continue;
					if(mp.find(s[k] - df) == mp.end()) {
					    //printf("N %d %d %d %lld %lld\n",i,j, k,s[k], df);
                            can=false;break;
                    }
					id = mp[s[k] - df];
					if(tmp[id] < tmp[k]) {
                            //printf("L %d %d\n",i,j);
					    can=false;break;
                    }
					tmp[id] -= tmp[k];
				}
				if(can)
				{
					id = -1;
					for(int k = 0; k < n; ++k) tmp[k] = cnt[k];
					for(int k = 0; k < n; ++k) cnt[k] = 0;
					for(int k = n - 1; k >= 0; --k)
					{
					    if(!tmp[k]) continue;
						id = mp[s[k] - df];
						tmp[id] -= tmp[k];
						if(df == s[j]) cnt[id] = tmp[k];
						else cnt[k] = tmp[k];
					};
					//printf("I %lld\n", s[j]);
					ret[i] = s[j];
					break;
				}
			}
		}
		printf("Case #%d:",ca);
		for(int i = 0; i < m; ++i) printf(" %d", ret[i]);
		puts("");
	}
	return 0;
}
