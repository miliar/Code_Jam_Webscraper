#include <iostream>
#include <string.h>
#include <set>
#include <stdio.h>
#include <queue>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
#define ll long long
const ll mod=1000002013;
const ll N=209;
struct node
{
    ll st,p;
    bool operator <(node a) const
    {
        return  st>a.st;
    }
};
multiset<node>g,tmp;

struct node2
{
    ll tim,p;
}a[N];
ll n,m;
bool cmp(node2 a,node2 b)
{
    if(a.tim!=b.tim)
    return a.tim<b.tim;
    return a.p>b.p;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll w;cin>>w;
    ll ca=1;
    while(w--)
    {
        printf("Case #%I64d: ",ca++);
        scanf("%I64d%I64d",&n,&m);
        ll ans1=0;
        for(ll i=0;i<m;i++)
        {
            ll s,t,p;
            scanf("%I64d%I64d%I64d",&s,&t,&p);
            ll cut=t-s;
            ans1=(ans1+p*(n*2-cut+1)*cut/2)%mod;
            a[i<<1].tim=s;
            a[i<<1].p=p;
            a[i<<1|1].tim=t;
            a[i<<1|1].p=-p;
        }
        sort(a,a+m*2,cmp);

        ll ans=0;
        g.clear();
        set<node> ::iterator p;
        ll starttime=0;
        for(ll i=0;i<m*2;i++)
        {
            tmp.clear();
            ll line=a[i].tim;
            for(p=g.begin();p!=g.end();p++)
            {
                ll peo=(*p).p;
                ll org=(*p).st;
                ll cut=line-starttime;
                ans=(ans+peo*(2*org-cut+1)*cut/2)%mod;
                node OK;
                OK.st=org-cut;
                OK.p=peo;
                tmp.insert(OK);
            }
           // cout<<"start= "<<starttime<<" line= "<<line<<" ans= "<<ans<<endl;
            starttime=line;
            g=tmp;
            if(a[i].p>0)
            {
                node OK;
                OK.st=n;
                OK.p=a[i].p;
                g.insert(OK);
            }else
            {
                ll out=-a[i].p;
                while(out&&(*g.begin()).p<=out)
                {
                    out-=(*g.begin()).p;
                    p=g.begin();
                    g.erase(p);
                }
                if(out)
                {
                    node fir=*g.begin();
                    p=g.begin();
                    g.erase(p);
                    fir.p-=out;
                    g.insert(fir);
                }
            }
            //for(p=g.begin();p!=g.end();p++) prllf("**%d %d\n",(*p).st,(*p).p);
        }
        cout<<(ans1-ans+mod)%mod<<endl;
    }


//    cout << "Hello world!" << endl;
    return 0;
}
