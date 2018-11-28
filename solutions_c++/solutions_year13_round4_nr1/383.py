#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define MOD (1000002013)

long long n;
int m;
long long o[1000], e[1000], num[1000];
vector<long long> x;
long long list[2010];

int main()
{
    int T;
    scanf("%d", &T);
    for(int cnt=1; cnt<=T; ++cnt)
    {
        x.clear();
        scanf("%lld %d", &n, &m);
        long long ans = 0;
        for(int i=0; i<m; ++i)
        {
            scanf("%lld %lld %lld", &o[i], &e[i], &num[i]);
            x.push_back(o[i]);
            x.push_back(e[i]);
            long long len = e[i]-o[i];
            ans += (len*n-len*(len-1)/2)%MOD*num[i];
            ans = (ans+MOD)%MOD;
        }
        sort(x.begin(), x.end());
        x.erase(unique(x.begin(), x.end()), x.end());
        memset(list, 0, sizeof(list));
        for(int i=0; i<m; ++i)
        {
            int from = lower_bound(x.begin(), x.end(), o[i])-x.begin();
            int to = lower_bound(x.begin(), x.end(), e[i])-x.begin();
            for(; from<to; ++from) list[from]+=num[i];
        }
        for(int i=0; i<x.size(); ++i)
            while(list[i]!=0)
            {
                int j=i+1;
                long long now = list[i];
                for(;j<x.size()&&list[j]!=0;++j) now = min(now, list[j]);
                long long len = x[j]-x[i];
                ans -= (len*n-len*(len-1)/2)%MOD*now%MOD;
                ans = (ans+MOD)%MOD;
                for(int k=i; k<j; ++k) list[k]-=now;
            }
        printf("Case #%d: %lld\n", cnt, ans);
    }
    return 0;
}
