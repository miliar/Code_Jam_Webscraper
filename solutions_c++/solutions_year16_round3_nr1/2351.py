#include<bits/stdc++.h>
#define pf printf
#define sf scanf
#define ll  long long
#define llu unsigned long long
#define M 50
#define pb push_back
#define ppb pop_back
#define F first
#define S second
#define Check(x,w) (x&(1<<w))==(1<<w)?true:false
#define pii pair<int,int>
#define EPS 1e-9
#define PI acos(-1)
#define Mems(p,n) memset(p,n,sizeof(p))
#define MOD 1000007
#define X 1300000
using namespace std;

template<class T>
inline bool fs(T &x)
{
    int c=getchar();
    int sgn=1;
    while(~c&&c<'0'||c>'9')
    {
        if(c=='-')sgn=-1;
        c=getchar();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=getchar())
        x=x*10+c-'0';
    x*=sgn;
    return ~c;
}

vector<pii>v;
int n;

bool comp(pii a,pii b)
{
    return a.F>b.F;
}

int main()
{
    freopen("inB.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt,i,j,a,b,c,d;
    fs(tt);
    pii u;
    for(t=1; t<=tt; t++)
    {
        fs(n);
        v.clear();
        for(i=0; i<n; i++)
        {
            fs(u.F);
            u.S=i;
            v.pb(u);
        }
        sort(v.begin(),v.end(),comp);
        vector<pii>x,res;
        while(1)
        {
            a=v.size();
            if(a==0)
                break;
            if(a>2 && v[0].F==v[1].F && v[0].F==v[2].F)
            {
                v[0].F--;
                res.pb(pii(v[0].S,-1));
                //pf("F=%d S=%d\n",v[0].S,v[1].S);
            }
            else if(a>1 && v[0].F==v[1].F)
            {
                v[0].F--;
                v[1].F--;
                res.pb(pii(v[0].S,v[1].S));
                //pf("F=%d S=%d\n",v[0].S,v[1].S);
            }
            else
            {
                v[0].F--;
                d=-1;
                res.pb(pii(v[0].S,d));
                //pf("F=%d D=%d\n",v[0].S,d);
            }
            for(i=0; i<a; i++)
            {
                //pf("%d F=%d S=%d\n",i,v[i].F,v[i].S);
                if(v[i].F>0)
                    x.pb(v[i]);
            }
            sort(x.begin(),x.end(),comp);
            v=x;
            x.clear();
        }
        pf("Case #%d:",t);
        for(i=0; i<res.size(); i++)
        {
            pf(" %c",res[i].F+'A');
            if(res[i].S!=-1)
                pf("%c",res[i].S+'A');
        }
        pf("\n");
    }
    return 0;
}
