#define LOCAL
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef double DB;
const int maxn=25+5;
const int INF=(1<<30);
int N;
vector<int> order;
bool dfs(int now,int S,int state)
{
    if(now==N) return 1;
    int p=order[now];
    bool flag=0;
    for(int i=p*N;i<p*N+N;i++)
    {
        if(!(S&(1<<i))) continue;
        if(!(state&(1<<(i%N))))
        {
            if(!dfs(now+1,S,state|(1<<(i%N)))) return 0;
            else flag=1;
        }
    }
    if(flag) return 1;
    else return 0;
}
int main()
{
#ifdef LOCAL
    freopen("Din","r",stdin);
    freopen("Dout","w",stdout); 
#endif
    int T,kase=0;
    scanf("%d",&T);
    while(T--)
    {
        int init=0;
        scanf("%d",&N);
        order.clear();
        for(int i=0;i<N;i++) order.push_back(i);
        char able[maxn];
        for(int i=0;i<N;i++)
        {
            scanf("%s",able);
            for(int j=0;j<N;j++) if(able[j]=='1') init|=(1<<(i*N+j));
        }
        int ans=INF;
        for(int S=init;S<(1<<N*N);S++)
        {
            if((S|init)!=S) continue;
            int cost=0;
            for(int i=0;i<N*N;i++) if( ((1<<i)&S) ^ ((1<<i)&init) ) cost++;
            if(cost>=ans) continue;
            sort(order.begin(),order.end());
            bool flag=1;
            do
            {
                if(!dfs(0,S,0)) {flag=0;break;}
            }while(next_permutation(order.begin(),order.end()));
            if(flag) ans=min(ans,cost);
        }
        printf("Case #%d: %d\n",++kase,ans);
    }
}
