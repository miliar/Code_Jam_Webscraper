#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll ans[105][105];

int main()
{
    ll t, k[105], c, s, p, i, j, l;
    cin>>t;
    for(l=1; l<=t; l++)
    {
        cin>>k[l]>>c>>s;
        p=pow(k[l], c);
        if(c==1)
        {
            for(i=0; i<k[l]; i++)
                ans[l][i]=i+1;
        }
        else
        {
            for(i=0; i<k[l]; i++)
                ans[l][i]=(k[l]*i)+i+1;
        }
        //cout<<l;
    }
    for(l=1; l<=t; l++)
    {
        cout<<"Case #"<<l<<": ";
        for(i=0; i<k[l]; i++)
            cout<<ans[l][i]<<" ";
        cout<<endl;
    }
    return 0;
}
