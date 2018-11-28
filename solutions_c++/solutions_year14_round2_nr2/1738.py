#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{

freopen("B-small-attempt0.in","r",stdin);
freopen("output","w",stdout);

int t,N,a,b,total,l,d,c,k;

scanf("%d",&t);
for(l=1;l<=t;l++)
{
   total = 0;
   scanf("%d %d %d",&a,&b,&k);

   for(c=0;c<a;c++)
   {
     for(d=0;d<b;d++)
     {
       N = c & d;
       if(N<k)
       total++;
     }

   }
   printf("Case #%d: %d\n",l,total);


}
return 0;
}

