#define LOCAL
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef double DB;
const int maxn=200+5;
DB prob[maxn];
int main()
{
#ifdef LOCAL
    freopen("Bin","r",stdin);
    freopen("Bout","w",stdout); 
#endif
    int T,kase=0;
    scanf("%d",&T);
    while(T--)
    {
        int N,K;
        scanf("%d%d",&N,&K);
        for(int i=0;i<N;i++) scanf("%lf",prob+i);
        DB ans=0;
        for(int S=0;S<(1<<N);S++)
        {
            int cnt=0;
            for(int i=0;i<N;i++) if((1<<i)&S) cnt++;
            if(cnt!=K) continue;

            vector<int> vec;
            for(int i=0;i<N;i++) if((1<<i)&S) vec.push_back(i);
            DB now=0;
            for(int SS=0;SS<(1<<K);SS++)
            {
                cnt=0;
                for(int i=0;i<K;i++) if((1<<i)&SS) cnt++;
                if(cnt!=K/2) continue;
                DB nownow=1;
                for(int i=0;i<K;i++) if((1<<i)&SS) nownow*=prob[vec[i]]; else nownow*=(1.0-prob[vec[i]]);
                now+=nownow;
            }
            ans=max(ans,now);
        }
        printf("Case #%d: %.6f\n",++kase,ans);
    }
}

