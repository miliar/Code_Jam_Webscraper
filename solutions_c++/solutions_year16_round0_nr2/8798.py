#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{   freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
   ll k,t;
   cin>>t;

   for(k=1;k<=t;k++)
   {
       ll i,j,ans=0;
       string s;
       cin>>s;
       int flag;
       while(1)
       {   if(s[0]=='-')flag=0;
           else         flag=1;
           int f=0;
           for(i=1;i<s.size();i++)
           {

               if(s[i]!=s[i-1])
               {
                   f=1;break;
               }
           }
           if(s.size()==1 || s.size()==0 || f==0)break;
           for(i=1;i<s.size();i++)
           {
               if(flag==0)
               {

                   if(s[i]=='-')
                      continue;
                   else
                   {

                       for(j=0;j<=i-1;j++)
                          s[j]='+';

                       break;
                   }
               }
               else
               {
                    if(s[i]=='+')
                          continue;
                       else
                       {

                           for(j=0;j<=i-1;j++)
                              s[j]='-';

                           break;

                       }


               }
           }






         ans++;
       }
       if(s[0]=='-')ans++;
       cout<<"Case #"<<k<<": "<<ans<<endl;
   }
    return 0;
}
