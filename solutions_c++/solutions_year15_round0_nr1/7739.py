#include<bits/stdc++.h>

#define mem(x,y) memset(x,y,sizeof(x))
#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)
#define diff(a,b) ((a<b)?b-a:a-b)
#define clrstr(a) memset(a,'\0',sizeof(a))
#define CLR(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define sz(a) a.size()
#define all(x) (x).begin(),(x).end()
#define pii pair<int,int>
#define pb(a) push_back(a)
#define pi 2*acos(0)
#define LL long long
#define rep(i,x) for(i=0;i<x;i++)
#define repv(i,v) for(i=0;i<v.size();i++)

#define EPS 1e-9
#define inf 10000000
#define MX 100000

using namespace std;

string s;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("ALarge.in","r",stdin);
    freopen("ALarge.out","w",stdout);

    long long n,t,ks,ppl,need,i;
    cin>>t;
    for(ks=1;ks<=t;ks++)
        {
            cin>>n>>s;
            ppl=0;
            need=0;

            for(i=0;i<=n;i++)
                {
                    if(i>ppl) need+=(i-ppl),ppl+=(i-ppl);
                    ppl+=(s[i]-'0');
                }

            cout<<"Case #"<<ks<<": "<<need<<endl;
            s.clear();
        }
}
