#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
long long int mod = 1000002013;
struct data
{
    long long int loc, num,goal;
    const bool operator < (const data& p) const
    {
        return loc<p.loc;
    }
};
struct train
{
    long long int loc,num,goal;
    bool type;
    const bool operator < (const train& p) const
    {
        return loc==p.loc? type<p.type: loc<p.loc;
    }
};
long long int f(long long int p)
{
    return (((p-1)*p)/(long long int)(2))%mod;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,t;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        int n,m;
        long long int answer=0;
        scanf("%d %d",&n,&m);
        int i,j;
        vector<train> a;
        for(i=0;i<m;i++)
        {
            int st,en,tmp;
            scanf("%d %d %d",&st,&en,&tmp);
            train tmpt;
            tmpt.loc = st;
            tmpt.num = tmp;
            tmpt.type = 0;
            tmpt.goal = en;
            a.push_back(tmpt);
            tmpt.loc = en;
            tmpt.type = 1;
            a.push_back(tmpt);
        }
        priority_queue<data> Q;
        sort(a.begin(),a.end());
        for(i=0;i<a.size();i++)
        {
            if(a[i].type==0)
            {
                data tp;
                tp.loc = a[i].loc;
                tp.num = a[i].num;
                tp.goal = a[i].goal;
                Q.push(tp);
            }
            else
            {
                while(a[i].num>0)
                {
                    data tp = Q.top();
                    Q.pop();
                    if(a[i].num >= tp.num)
                    {
                        a[i].num-=tp.num;
                        answer += (((f(a[i].loc - tp.loc) - f(tp.goal-tp.loc))%mod)*tp.num)%mod;
                        answer%=mod;
                    }
                    else
                    {
                        tp.num -= a[i].num;
                        answer += (((f(a[i].loc - tp.loc) - f(tp.goal-tp.loc))%mod)*a[i].num)%mod;
                        a[i].num=0;
                        answer%=mod;
                        Q.push(tp);
                    }
                }
            }
        }
        printf("Case #%d: %lld\n",t,((answer%mod)+mod)%mod);
    }
    return 0;
}
