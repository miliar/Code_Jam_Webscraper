#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define ll long long
#define pil pair<ll, ll>
#define MP make_pair
#define F first
#define S second

using namespace std;

const ll MOD = 1000002013LL;

ll T, M;
ll N;
vector<pil> data;

bool cmp(const pil &a, const pil &b)
{
	if(a.F==b.F)return a.S>b.S;
	else return a.F<b.F;
}

ll cost(const ll dis, const ll num)
{
	ll tmp = (dis*N - dis*(dis-1)/2) % MOD;
	return (tmp * num) % MOD;
}

int main()
{
    ios_base::sync_with_stdio(0);

    cin>>T;
    for(int t=1; t<=T; t++)
	{
		cin>>N>>M;
		ll origcost = 0;
		data.clear();
		for(int i=0; i<M; i++)
		{
			ll o, e, p;
			cin>>o>>e>>p;
			ll dis = e - o;
			origcost += cost(dis, p);
			origcost %= MOD;
			data.push_back(MP(o, p));
			data.push_back(MP(e, -p));
		}
		sort(data.begin(), data.end(), cmp);
		vector<pil> stk;
		ll ans = 0;
		for(int i=0; i<(int)data.size(); i++)
		{
			ll a = data[i].F;
			ll b = data[i].S;
			//cout<<"("<<a<<","<<b<<")"<<endl;
			if(b>0)
			{
				stk.push_back(MP(a, b));
			}
			else
			{
				ll rem = -b;
				while(rem>0)
				{
					ll red = stk.back().S, dis = a - stk.back().F;
					if(rem >= red)
					{
						rem -= red;
						ans += cost(dis, red);
						//cout<<"+"<<cost(dis, red)<<endl;
						stk.pop_back();
					}
					else
					{
						ans += cost(dis, rem);
						stk.back().S -= rem;
						//cout<<"+"<<cost(dis, rem)<<endl;
						rem = 0;
					}
					ans %= MOD;
				}
			}
		}
		//cout<<ans<<" / "<<origcost<<endl;
		ll trueans = (origcost%MOD - ans%MOD + MOD) % MOD;
		cout<<"Case #"<<t<<": "<<trueans<<endl;
	}

    return 0;
}
