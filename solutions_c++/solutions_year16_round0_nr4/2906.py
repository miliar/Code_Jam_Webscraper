#include<iostream>
using namespace std;
int main()
{
    int k,t,c,s,i,ans,l;
    cin>>t;
    for(i=1;i<=t;++i)
    {
    cin>>k>>c>>s;
            if(k<=s)
            {
            cout<<"Case #"<<i<<":";
            for(l=1;l<=s;++l)
            cout<<" "<<l;
            cout<<endl;
            }
            else
            {
                 ans=0;
                cout<<"Case #"<<i<<":";
                    if(c==1)
                    cout<<" IMPOSSIBLE";
                    else
                    {
                        for(l=2;l<=k*k;l=l+k+1)
                        ++ans;
                        if(k==2)
                        ans=2;
                        if(ans>s)
                        cout<<" IMPOSSIBLE";
                        else
                        for(l=2;l<=k*k;l=l+k+1)
                        cout<<" "<<l;
                    }
                cout<<endl;
            }
     }
     cin>>l;
    return 0;
}
