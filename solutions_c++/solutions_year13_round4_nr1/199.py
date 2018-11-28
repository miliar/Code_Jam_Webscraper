#include<cstdio>
#include<map>
#include<stack>
#define MOD 1000002013
using namespace std;
map<pair<long long,long long>,long long> M;
stack<pair<long long,long long> > S;
long long dist (long long o,long long e,long long p)
{
    long long d = (e-o);
    if (d%2==0)
        d = d/2*(d+1);
    else
        d = (d+1)/2*d;
    d %= MOD;
    d *= p;
    d %= MOD;
    return d;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    long long T,tt,i,n,m,o,e,p,c;
    long long gain,loss;
    map<pair<long long,long long>,long long>::iterator it;
    scanf("%I64d",&T);
    for (tt=1;tt<=T;tt++)
    {
        M.clear();
        scanf("%I64d %I64d",&n,&m);
        gain = 0;
        loss = 0;
        for (i=0;i<m;i++)
        {
            scanf("%I64d %I64d %I64d",&o,&e,&p);
            gain += dist(o,e,p);
            gain %= MOD;
            M[make_pair(o,1)] += p;
            M[make_pair(e,2)] += p;
        }
        for (it=M.begin();it!=M.end();it++)
        {
            if (it->first.second==1)
                S.push(make_pair(it->first.first,it->second));
            else if (it->first.second==2)
            {
                c = it->second;
                while (c-S.top().second>=0)
                {
                    c -= S.top().second;
                    loss += dist(S.top().first,it->first.first,S.top().second);
                    loss %= MOD;
                    S.pop();
                    if (S.empty())
                        break;
                }
                if (!S.empty() and c>0)
                {
                    loss += dist(S.top().first,it->first.first,c);
                    loss %= MOD;
                    o = S.top().first;
                    e = S.top().second-c;
                    S.pop();
                    S.push(make_pair(o,e));
                }
            }
        }
        printf("Case #%I64d: %I64d\n",tt,(loss-gain+MOD)%MOD);
    }
    return 0;
}
