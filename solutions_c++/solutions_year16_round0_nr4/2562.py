#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in","rt",stdin);
	freopen("outs.out","wt",stdout);
	int t,k,c,s;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        if(k>s)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            for(int j=1;j<=k;j++)
                cout<<j<<" ";
        }
        cout<<"\n";
    }
    return 0;

}
