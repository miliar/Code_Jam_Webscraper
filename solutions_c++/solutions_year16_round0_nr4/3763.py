#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int tt;
    cin>>tt;
    for(int i=1; i<=tt; i++)
    {
       int k,c,s;
       cin>>k>>c>>s;
       cout<<"Case #"<<i<<": ";
       for(int j=1;j<=k;j++)
           cout<<" "<<j;

       cout<<endl;
    }
    return 0;
}
