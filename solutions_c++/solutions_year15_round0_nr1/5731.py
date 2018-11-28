#include <bits/stdc++.h>
using namespace std;
bool comp(int a,int b)
{
    return (a>b);
}
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(void) {
    freopen("in.txt","rt",stdin);
    freopen("test.txt","wt",stdout);
    int t,n,i;
    string s;
    cin>>t;
    for(i=1;i<=t;++i)
    {
        cin>>n>>s;
        cout<<"Case #"<<i<<": ";
        int j,c=0,ans=0;
        for(j=0;j<=n;++j)
        {
            if(s[j]!='0')
            {
                if(c<j)
                {
                    ans+=(j-c);
                    c=j;
                }
                c+=(s[j]-'0');
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}
