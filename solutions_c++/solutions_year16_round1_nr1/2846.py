#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define repm(i,a,b) for(int i=(a);i>(b);i--)
#define f(i,n) rep(i,0,n)
#define pin(n) printf("%d\n",n)
#define si(n) scanf("%d",&n)
#define sii(m,n) scanf("%d %d",&m,&n)
#define pb push_back
typedef long long ll;
#define mod 1000000007

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int q;
    si(q);
    f(i,q)
    {
        string s;
        cin>>s;
        int l=s.size();
        string ans=s.substr(0,1);
        f(j,l-1)
        {
            if(s[j+1]>=ans[0]) ans.insert(0,s,j+1,1);
            else ans+=s.substr(j+1,1);
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}




































