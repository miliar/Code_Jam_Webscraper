#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define ll long long 
#define oo 1000000000
using namespace std;  
ll s[50],a,b;
int main()
{ 
      FILE *f1=fopen("generator.txt","r");
      int i;
      for (i=1;i<=48;i++) fscanf(f1,"%I64d",&s[i]);  
    //  freopen("C-large-1.in","r",stdin);
   //   freopen("output.txt","w",stdout);
      int T,t,na,nb; 
      scanf("%d",&T);
      for (t=1;t<=T;t++)
      {
            scanf("%I64d%I64d",&a,&b);
            a--;
            na=0;
            while (na!=48 && s[na+1]<=a) na++;
            nb=0;
            while (nb!=48 && s[nb+1]<=b) nb++;
            nb-=na; 
            printf("Case #%d: %d\n",t,nb);
      }
      return 0;
}
