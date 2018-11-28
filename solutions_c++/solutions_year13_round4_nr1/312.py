#include <cstdio>
#include <set>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

int N, M;

typedef pair<int, int> PI;
typedef pair<int, PI> PII;

PII buf[100000];
int total;
const int MOD =  1000002013;
long long int f(int a, int b)
{
    b -= a;
    return b * (N + (N - b + 1ll)) / 2 % MOD;    
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int tn = 1; tn <= T; tn++)
    {
	printf("Case #%d: ", tn);
	scanf("%d%d", &N, &M);
	int ans = 0;
	int ans2 = 0;

	total = 0;
	for(int i = 0; i < M; i++)
	{
	    int o, e, p;
	    scanf("%d%d%d", &o, &e, &p);

	    ans2 = (ans2 + f(o, e) * p % MOD) % MOD;
	    buf[total++] = PII(o, PI(0, p));
	    buf[total++] = PII(e, PI(1, p));	    
	}
	sort(buf, buf + total);


	multiset<pair<int, int>, greater<pair<int, int> > > table;
	for(int i = 0; i < total; i++)
	    if(buf[i].second.first == 0)
		table.insert(make_pair(buf[i].first, buf[i].second.second));
	    else while(buf[i].second.second)
	    {
		long long int t = min(table.begin()->second, buf[i].second.second);
   	        ans = (ans + (f(table.begin()->first, buf[i].first) * t % MOD)) % MOD;

		int l = table.begin()->first;
		int r = table.begin()->second - t;		
		if(r)
		    table.insert(make_pair(l, r));
  	        table.erase(table.begin());
		buf[i].second.second -= t; 
	    }

	ans = (ans2 - ans + MOD) % MOD;
	printf("%d\n", ans);
    }
    return 0;
}
