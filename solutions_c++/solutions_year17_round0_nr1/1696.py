#include <bits/stdc++.h>
#define ll long long
#define inf 1000000000
#define pb push_back
using namespace std;
string str;
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    int n,m,i,j,k,l,t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<": ";
        cin>>str>>k;
        bool flag=0;
        n=str.size();
        int ans=0;
        for(i=0;i<n;i++)
        {
            if(str[i]=='-'&&i+k-1<n)
            {
                ans++;
                //cout<<i<<" ";
                for(j=i;j<i+k;j++){
                    if(str[j]=='-')
                    str[j]='+';
                    else
                    str[j]='-';
                    //cout<<str[j]<<" ";
                }
            }
            else
            if(str[i]=='-')
                    {
                      //  cout<<i<<" ";
                        flag=1;
                        break;
                    }
        }
        if(flag)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<"\n";
    }
    return 0;
}
