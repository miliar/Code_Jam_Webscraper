#include <bits/stdc++.h>
#define ull unsigned long long int
using namespace std;
ull power(ull a, ull b)
{

    if(b==0)return 1;

    ull ans=power(a,b/2);
    ans=ans*ans;

    if(b&1)///odd
        ans=ans*a;

    return ans;
}
int main()
{
    int t;
    cin>>t;
    ull i,cs,k,c,s,x;
    for(cs=1;cs<=t;cs++)
    {

        cout<<"Case #"<<cs<<": ";
        cin>>k>>c>>s;
        if(s==k)
        {
            x=power(k,c-1);
            for(i=1;i<=k;i++)
            {
                cout<<i*x<<" ";
            }
            cout<<endl;
        }
    }
}
