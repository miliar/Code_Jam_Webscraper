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
#define SZ 1005
#define MOD 1000002013

vector<pair<pair<int, int>, int> > dat;
int pps[SZ][SZ];
int sts[SZ];
int ens[SZ];
long long tot;



int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);


	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int inp, kase, i, j, k, a, n, m;
	int st, en, p;
	
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &m);
		long long sum1 = 0;
		tot = n;
		dat.clear();
		for(i = 0; i < m; i++)
		{
			scanf("%d %d %d", &st, &en, &p);
			dat.push_back(make_pair(make_pair(st, 0), p));
			dat.push_back(make_pair(make_pair(en, 1), p));
			long long diff = en - st;
			long long tmpp = ((diff * n) - (diff * (diff - 1)) / 2) % MOD;
			sum1 = (sum1 + tmpp * p) % MOD;
		}
		sort(dat.begin(), dat.end());
		
		long long sum = 0;
		long long tmp = 0;
		for(i = 0; i < dat.size(); i++)
		{
			if(dat[i].first.second == 1)
			{
				int tp = dat[i].second;
				long long cen = dat[i].first.first;
				for(j = i - 1; j >= 0; j--)
				{
					if(dat[j].first.second == 0)
					{
						long long dif = cen - dat[j].first.first;
						tmp = (dif * n - (dif * (dif - 1)) / 2) % MOD;
						if(dat[j].second > tp)
						{
							sum = (sum + tmp * tp) % MOD;
							dat[j].second -= tp;
							tp = 0;
							break;
						}
						else
						{
							sum = (sum + tmp * dat[j].second) % MOD;
							tp -= dat[j].second;
							dat[j].second = 0;
						}
					}
				}
			}
		}
		sum = (sum1 - sum + MOD) % MOD;
		printf("Case #%d: %lld\n", kase, sum);
	}

	return 0;
}

