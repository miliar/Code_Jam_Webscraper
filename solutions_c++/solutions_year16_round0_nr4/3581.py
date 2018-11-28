#include<bits/stdc++.h>
using namespace std;
int main()
{
   // ios_base::sync_with_stdio(false);
    //cin.tie(false);
    int t;
    cin>>t;
    int h=1;
    while(t--)
    {
        int k,c,s;
        cin>>k>>c>>s;
        if(k==1)
            cout<<"Case #"<<h<<":"<<" "<<"1\n";
            else
            {
                if(c==1)
                {
                    if(s>=k)
                    {
                          cout<<"Case #"<<h<<":"<<" ";
                        for(int j=1;j<=k;j++)
                        {
                           cout<<j<<" ";
                        }
                        cout<<"\n";
                    }
                    else
                         cout<<"Case #"<<h<<":"<<" "<<"IMPOSSIBLE\n";
                }
                else
                {
                    if(s>=k-1)
                    {
                        cout<<"Case #"<<h<<":"<<" ";
                        for(int j=2;j<=k;j++)
                        {
                           cout<<j<<" ";
                        }
                          cout<<"\n";
                    }
                    else
                    cout<<"Case #"<<h<<":"<<" "<<"IMPOSSIBLE\n";

                }
            }
            h++;
    }
    return 0;
}
