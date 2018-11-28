#include<bits/stdc++.h>
#define ll long long
#define pf printf
#define sc scanf
using namespace std;

string s;
ll l;

 bool check(void)
 {
     bool f=true;
     for(ll i=0;i<l;i++)
     {
         if(s[i]=='-')
         {
             f=false;
             break;
         }
     }
     if(!f)
        return false;
     return true;

 }

int main()
{
     freopen("B-large.in","r",stdin);
     freopen("A.out","w",stdout);
    ll t,last,cnt;

    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cin>>s;
        pf("Case #%lld: ",i);
        cnt=0;
         l=s.size();

         while(!check())
         {
             cnt++;
            for(ll j=l-1;j>=0;j--)
            {
                if(s[j]=='-')
                {
                    last=j;
                    break;
                }
            }
            for(ll j=0;j<=last;j++)
            {
                if(s[j]=='+')
                    s[j]='-';
                else
                    s[j]='+';
            }
         }
         cout<<cnt<<endl;
    }

return 0;
}
