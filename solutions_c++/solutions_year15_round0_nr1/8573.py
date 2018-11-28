#include<iostream>
#include<cstdio>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
using namespace std;

int main()
{
   int t,n,c=0,ans,i,j=1;
   FILE *f,*fo;
   f=fopen("A-large.in","r");
   fo=fopen("output.txt","w");
   char s[1005];
   fscanf(f,"%d",&t);
   //cout<<t<<endl;
   while(t--)
   {
       ans=0;
       fscanf(f,"%d %s",&n,s);
       c=s[0]-'0';
       for(i=1;i<=n;i++)
       {
           if(c<i)
           {
               ans=ans+i-c;
               c=i;
           }
           c=c+s[i]-'0';
       }
       fprintf(fo,"Case #%d: %d\n",j,ans);
       j++;
   }
   return 0;
}
