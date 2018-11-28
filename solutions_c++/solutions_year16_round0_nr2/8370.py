#include<bits/stdc++.h>
using namespace std;
#define ll long long int

bool has(string k)
{
 ll l=k.size();
 for(ll i=0;i<l;i++)
 {
   if(k[i]=='-')
   return true;
 }
 return false;

}

bool allneg(string s)
{
 for(ll i=0;i<s.size();i++)
 {
  if(s[i]=='+')
  return false;
 }

 return true;

}

bool alltru(string s)
{
 for(ll i=0;i<s.size();i++)
 {
  if(s[i]=='-')
  return false;
 }

 return true;

}

int main()
{
   ll t; string d;ll cnt=0;
   scanf("%lld",&t);
   getline(cin,d);
   for(ll i=1;i<=t;i++)
   {cnt=0;
     printf("Case #%d: ",i);

     string k,cpy;
     getline(cin,k);
     ll l=k.size();


 for(ll j=0;j<l;j++)
     {
       cpy+=k[j];
     }

   while(1)
     { //cout<<cpy<<endl;


      if(allneg( cpy))
      {
       printf("%lld\n",cnt+1);
           break;
      }

      else if(alltru(cpy))
      {

       printf("%lld\n",cnt);
           break;
      }
      else if(has(cpy))
      {
       if(cpy[0]=='+')
       {
        for(ll j=0;j<cpy.size();j++)
        {

         cpy[j]='-';
         if(cpy[j+1]=='-')
         {
           break;
         }
        }
       }

       else if(cpy[0]=='-')
       {
        for(ll j=0;j<cpy.size();j++)
        {

         cpy[j]='+';
         if(cpy[j+1]=='+')
         {
           break;
         }
        }


       }

      }
     cnt++;
     }



   }
  return 0;
}

