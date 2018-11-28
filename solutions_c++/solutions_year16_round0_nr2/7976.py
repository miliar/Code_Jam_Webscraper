#include <bits/stdc++.h>
#define MOD 1000000007
using namespace std;

long long ar[1000002];
set<long long> st;

int main()
{
   freopen("inp.txt","r",stdin);
   freopen("op.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    long long n,m,a,b,i,j,val=0,ans=0,x,y,t,T;
    cin>>T;
    string s;
    for(t=1;t<=T;t++)
    {
        ans=0;
        cin>>s;
        for(i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                ans++;
                s[i]='+';
                j=i-1;
                while(j>=1 && s[j]=='-')
                {
                    s[j]='+';
                    j--;
                }
                i=j;
                for(j=i;j>=0;j--)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                i++;
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
}