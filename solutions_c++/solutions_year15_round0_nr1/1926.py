#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#define oo 105
using namespace std; 
char s[1005];
int main()
{
      int Cases,cases,n,i,len,ans,sum,num;
      freopen("A-large.in","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&Cases);
      for (cases=1;cases<=Cases;cases++)
      {
              scanf("%d%s",&n,s),ans=sum=0,len=strlen(s);
              for (i=0;i<len;i++)
              {
                     if (sum<i) ans+=i-sum,sum=i;
                     sum+=s[i]-'0';
              }
              printf("Case #%d: %d\n",cases,ans);   
      }
      return 0;
}
