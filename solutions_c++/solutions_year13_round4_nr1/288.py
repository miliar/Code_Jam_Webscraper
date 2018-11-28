#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int,int> pii;
const int mod = 1000002013;
int calc(int s,int e,int m,int N)
{
    if (s==e) return 0;
    long long d = e-s;
    // N * d + d * (d-1) / 2 
    long long c = N*d - d*(d-1)/2;
    c %= mod;
    c *= m;
    c %= mod;
    return c;
}
int main()
{
    int T;scanf("%d",&T);
    for (int kase=1;kase<=T;++kase)
    {
        vector<pii> change;
        stack<pii> s;
        int N,M,must=0;
        scanf("%d %d",&N,&M);
        for (int q=0;q<M;++q)
        {
            int o,e,m;
            scanf("%d %d %d",&o,&e,&m);
            change.push_back(pii(o,-m));
            change.push_back(pii(e,m));
            must=(must+calc(o,e,m,N))%mod;
        }
        sort(change.begin(),change.end());
        int got = 0;
        for (int i=0;i<change.size();++i)
        {
            int ch = change[i].second;
            if (ch>0) //exit
            {
                while (ch>0)
                {
                    int bf = s.top().first;
                    int man = min(ch,s.top().second);
                    int cost = calc(bf, change[i].first, man,N);
                    got=(got+cost)%mod;
                    ch-=man;
                    s.top().second-=man;
                    if (s.top().second == 0) s.pop();
                }
            }
            else
            {
                change[i].second *= -1;
                s.push(change[i]);
            }
        }
        fprintf(stderr,"Case #%d: %d\n",kase,(-got+must+mod)%mod);
        printf("Case #%d: %d\n",kase,(-got+must+mod)%mod);
    }
    return 0;
}
