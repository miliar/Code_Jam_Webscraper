#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t,k,c,s;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<tc<<":";

        for(int i=1;i<=k;i++)
        {
            cout<<" "<<i;
        }
        cout<<endl;
    }

    return 0;
}
