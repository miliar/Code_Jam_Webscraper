#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        string a;
        cin>>a;
        ll ans=0,i,j;
        ll n=a.length();
        for(i=0;i<n-1;i++)
        {
            if(a[i]==a[i+1])
                continue;
            else
                ans++;
        }
        if(a[n-1]=='-')
            ans++;
        cout<<"Case #"<<q<<": "<<ans<<"\n";
    }
    return 0;
}
