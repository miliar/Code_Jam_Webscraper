#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
   //freopen("A-large.in","r",stdin);
   //freopen("A-large.out","w",stdout);
   char str[1100];
   int t,Smax,Case=0;
   scanf("%d",&t);
   while(t--)
   {
       scanf("%d%s",&Smax,str);
       int sum=0,ans=0;
       for(int i=0;i<=Smax;i++)
       {
           if(str[i]=='0')
              continue;
           if(sum<i)
           {
               ans+=(i-sum);
               sum=i+(str[i]-'0');
           }
           else
               sum+=(str[i]-'0');
       }
       printf("Case #%d: %d\n",++Case,ans);
   }
}
