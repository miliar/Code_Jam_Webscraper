#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int a[5]={1,4,9,121,484};
int main()
{
 int t,i,j,n,m,c,cas;
 scanf("%d",&t);
 for(cas=1;cas<=t;cas++)
 {
       scanf("%d%d",&n,&m);
       c=0;i=0; 
       while(i<5)
       {
       if((a[i]/n)>=1)
       {
                    if((a[i]/(m*1.0))<=1)
                    c++;
                    i++;
       }
       else
       i++;
       }
       printf("Case #%d: %d\n",cas,c);
 }
return 0;
}
