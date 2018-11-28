#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;
struct node
{
    int o,p;
}nt[2010];
bool cmp(const node&a,const node&b)
{
    return a.o==b.o?a.p>b.p:a.o<b.o;
}
const int mod=1000002013;
typedef long long ll;
int fun(int n,ll N,int p)
{
    ll ret=N*n%mod;
    ret-=(ll)(n)*(n+1)/2;
    ret%=mod;
    if(ret<0)ret+=mod;
    ret=ret*p%mod;
    //printf("dd%d %d %d\n",n,p,(int)ret);
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;scanf("%d",&n);
    for(int ca=1;ca<=n;ca++)
    {
        int n,m;scanf("%d%d",&n,&m);
        vector<node>list;
        int rr=0;
        for(int i=0;i<m;i++)
        {
            int o,e,p;scanf("%d%d%d",&o,&e,&p);
            nt[i*2].o=o;
            nt[i*2].p=p;
            nt[i*2+1].o=e;
            nt[i*2+1].p=-p;
            rr+=fun(e-o,n,p);
            if(rr>=mod)rr-=mod;
        }
        sort(nt,nt+m*2,cmp);
        priority_queue<pair<int,int> >que;
        int ret=0;
        for(int i=0;i<m+m;i++)
        {
            //printf("zz%d %d\n",nt[i].o,nt[i].p);
            if(nt[i].p>0)
            {
                que.push(make_pair(nt[i].o,nt[i].p));
            }
            else
            {
                int need=-nt[i].p;
                while(need>0)
                {
                    int o=que.top().first;
                    int p=que.top().second;
                    que.pop();
                    ret+=fun(nt[i].o-o,n,min(need,p));
                    if(ret>=mod)ret-=mod;
                    need-=p;
                    if(need<0)
                    {
                        que.push(make_pair(o,-need));
                    }
                }
            }
        }
        //printf("%d ",ret);
        ret=rr-ret;
        if(ret<0)ret+=mod;
        //printf("%d %d\n",rr,ret);
        printf("Case #%d: %d\n",ca,ret);
    }
}
