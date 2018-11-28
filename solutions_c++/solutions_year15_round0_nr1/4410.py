#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
typedef long long int ll;
using namespace std;
int main()
{
   FILE *op=fopen("output.in","w");
   FILE *ip=fopen("A-small-attempt0.in","rt");
ll t,t1,a,i,till,fr;
char s[10000];
fscanf(ip,"%lld",&t);
for(t1=1;t1<=t;t1++)
{
fscanf(ip,"%lld",&a);
fscanf(ip,"%s",s);
till=0;
fr=0;
for(i=0;i<=a;i++)
{
    if(i>till)
    {
       fr=fr+(i-till);
       till=till+(i-till)+(s[i]-'0');
    }
    till=till+(s[i]-'0');
}
 fprintf(op,"Case #%lld: %lld\n",t1,fr);
}
return 0;
}
