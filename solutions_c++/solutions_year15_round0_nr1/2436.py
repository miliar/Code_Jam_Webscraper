#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
 int main()
 {
     int t,j,ans,sum,n,i;
     char ch[1010];
     scanf("%d",&t);
     for(j=1;j<=t;j++)
     {
         scanf("%d",&n);
         scanf("%s",&ch);
         sum=0;
         ans=0;
         for(i=0;i<=n;i++)
         {
             if(ch[i]=='0')
                continue;
             if((sum)<i)
             {
               //  cout<<"needed"<<i<<endl;
                ans=ans+(i-sum);
                sum=sum+ch[i]-'0'+(i-sum);
             }
             else
             {
                 sum=sum+ch[i]-'0';
             }
         }
         printf("Case #%d: %d\n",j,ans);
     }
 }
