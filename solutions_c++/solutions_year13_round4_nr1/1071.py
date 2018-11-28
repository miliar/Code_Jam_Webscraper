#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <memory.h>
#include <cmath>
#include <deque>

using namespace std;
int n,m,t;
long long total1 = 0, total2 = 0;
long long mod =	1000002013;
vector<int> st;
vector<pair<int,int> > cur;
vector<pair<int,int> > v;

bool f(pair<int,int> a, pair<int,int> b)
{
	if (a.first < b.first)
		return 1;
	if ((a.first == b.first) && (a.second > b.second))
		return 1;
	return 0;
}
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int q = 1; q <= t; q++)
	{
		cur.clear();
		scanf("%d%d",&n,&m);
		v.clear();
		st.clear();
		total1 = 0;
		total2 = 0;
		for (int i = 0; i < m; i++)
		{
			int x,y,z;
			scanf("%d%d%d",&x,&y,&z);
			int diff = y - x - 1;
			total1 = (total1 + (((diff * (diff + 1) / 2) % mod) * z ) % mod) % mod;
			st.push_back(z);
			v.push_back(make_pair(x,(i+1)));
			v.push_back(make_pair(y,-(i+1)));
		}
		sort(v.begin(),v.end(), f);
		for (int i = 0; i < v.size(); i++)
		{
			if (v[i].second > 0)
			{
				cur.push_back(make_pair(v[i].first, st[v[i].second-1]));
			} else
			{
				int tmp = st[-v[i].second-1];
				while (tmp > 0)
				{
					pair<int,int> t = cur.back();
					int start = t.first;
					int cnt = t.second;
					int diff = v[i].first - start - 1;
					if (tmp >= cnt)
					{
						total2 = (total2 + (((diff * (diff + 1) / 2) % mod) * cnt)% mod) % mod;
						tmp -= cnt;
						cur.pop_back();
					} else
					{
						total2 = (total2 + (((diff * (diff + 1) / 2) % mod) * tmp)% mod) % mod;
						cur[cur.size()-1].second -= tmp;
						tmp = 0;
					}
				}
			}
		}
		printf("Case #%d: %lld\n", q, (total2 - total1 + mod) % mod);
	}
	return 0;
}