#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
map<long long,long long> mp;
vector<long long> sum,pos;
long long n;
long long money(long long d)
{
	if (d==0)
	{
		return 0;
	}
	long long ans=(n+n-d+1)*d/2;
	return ans;
}
long long md=1000002013;
int main()
{

	//freopen("E:\\gcj\\input.in","r",stdin);
	//freopen("E:\\gcj\\ouput.txt","w",stdout);
	int T;	
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		int m;
		cin >> n >> m;
		mp.clear();
		sum.clear();
		pos.clear();
		long long ori=0;
		for (int i=0;i<m;++i)
		{
			long long o,e,p;
			cin >> o >> e >> p;
			if (mp.count(o))
			{
				mp[o]+=p;
			}
			else
			{
				mp[o]=p;
			}
			if (mp.count(e))
			{
				mp[e]-=p;
			}
			else
			{
				mp[e]=-p;
			}
			long long tmp=money(e-o)%md;
			ori+=tmp*p;
			ori%=md;
		}
		for (map<long long,long long>::iterator it=mp.begin();it!=mp.end();++it)
		{
			sum.push_back(it->second);
			pos.push_back(it->first);
		}
		m=pos.size();
		long long mm=0;
		for (int i=0;i<m;++i)
		{
			if (sum[i]<0)
			{
				for (int j=i-1;j>=0;--j)
				{
					if (sum[i]==0)
					{
						break;
					}
					if (sum[j]>0)
					{
						long long mi=min(-sum[i],sum[j]);
						sum[i]+=mi;
						sum[j]-=mi;
						long long tmp=money(pos[i]-pos[j])%md;
						mm+=tmp*mi;
						mm%=md;
					}
				}
			}			
		}
		long long ans=(ori-mm+md*2)%md;
		printf("Case #%d: %lld\n",kk,ans);

	}
	return 0;
}