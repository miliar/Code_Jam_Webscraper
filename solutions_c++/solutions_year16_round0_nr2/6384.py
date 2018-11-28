#include <bits/stdc++.h>
#define fi first
#define se second
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
#define mod 1000000007
#define pb push_back
#define mp make_pair
using namespace std;

int main() {
    //fastio
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,n,j,f,k,ans;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        n=s.size();
        k=n-1;
        ans=0;
        f=0;
        while(f==0)
        {
            for(j=k;j>=0;j--)
            {
               if(s[j]=='-')
                    break;
            }
            if(j==-1)
            {
                cout<<"Case #"<<i<<": "<<ans<<endl;
                f=1;
                break;
            }
            k=j;
            for(j=k;j>=0;j--)
            {
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
            ans++;
        }
    }
}
