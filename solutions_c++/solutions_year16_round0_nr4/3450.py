#include<bits/stdc++.h>
using namespace std;

int main()
{
    int i,t,K=1;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<K++<<": ";
        if(s==k)
        {
            for(i=1;i<=k;i++)
            {
                cout<<i<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}
