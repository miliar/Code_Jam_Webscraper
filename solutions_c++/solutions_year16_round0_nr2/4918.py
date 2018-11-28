#include <bits/stdc++.h>
using namespace std;
int main()
{
   int t,n,x,rem,sum,ans,i,j,k;
   freopen("B-large.txt","rt",stdin);
   freopen("output.txt","wt",stdout);
   scanf("%d",&t);
   for(j=0;j<t;j++)
   {
       string s,sn;
       cin>>s;
       int l=s.length();
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
       int ll;
       if(sn[0]=='-')
       {
           ll=sn.length();
           if(ll%2)
           ans=ll;
           else
           ans=ll-1;
           printf("Case #%d: %d\n",j+1,ans);
           continue;
       }
       else
       {
          ll=sn.length();
           if(ll%2)
           ans=ll-1;
           else
           ans=ll;
           printf("Case #%d: %d\n",j+1,ans);
           continue;
       }
       //cout<<sn<<endl;
      // printf("Case #%d: %d\n",i+1,ans);
   }
   return 0;
}
