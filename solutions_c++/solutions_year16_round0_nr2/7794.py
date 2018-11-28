#include<bits/stdc++.h>
#define pf printf
#define sf scanf
#define ll  long long
#define llu unsigned long long
#define M 10000
#define pb push_back
#define ppb pop_back
#define F first
#define S second
#define Check(x,w) (x&(1<<w))==(1<<w)?true:false
#define pii pair<ll,ll>
#define X 5800000
#define PI acos(-1)
#define MOD 100000000
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

string s;

int main()
{
    freopen("inBL.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt;
    int a,b,c,d,e,l,i,j;
    fs(tt);
    for(t=1; t<=tt; t++)
    {
        cin>>s;
        l=s.size();
        while(s[l-1]=='+' && l>0)
            l--;
        if(l==0)
        {
            pf("Case #%d: 0\n",t);
            continue;
        }
        d=1;
        char x=s[0];
        for(i=1; i<l; i++)
        {
            if(s[i]!=x)
            {
                d++;
                x=s[i];
            }
        }
        pf("Case #%d: %d\n",t,d);
    }
    return 0;
}
