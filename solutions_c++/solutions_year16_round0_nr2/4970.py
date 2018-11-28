#include <bits/stdc++.h>
using namespace std;
int main()
{
   int t,n,x,rem,sum,ans,i,j,k,l,ll;
   freopen("B-large.txt","rt",stdin);
   freopen("output.txt","wt",stdout);
   cin>>t;
   for(j=0;j<t;j++)
   {
       string s,sn;
       cin>>s;
       l=s.length();
       for(i=0;i<l;)
       {
           if(s[i]=='-')
           {
               while(s[i]=='-'&&i<l)
               {
                   i++;
               }
               sn.push_back('-');
           }
           else if(s[i]=='+')
           {
               while(s[i]=='+'&&i<l)
               {
                   i++;
               }
               sn.push_back('+');
           }
       }
       ll=sn.length();
       if(sn[0]=='-')
       {
           if(ll%2)
           ans=ll;
           else
           ans=ll-1;
       }
       else
       {
           if(ll%2)
           ans=ll-1;
           else
           ans=ll;
       }
        cout<<"Case #"<<j+1<<": "<<ans<<endl;
   }
   return 0;
}
