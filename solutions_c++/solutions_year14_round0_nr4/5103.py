#include <stdio.h>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
  int main()
  {

   freopen("D-small-attempt2.in.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t,i,c,k,n,j;
   float an[10],ak[10];
   scanf("%d",&t);
for(k=1;k<=t;k++)
    {
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%f",&an[i]);

for(i=0;i<n;i++)
scanf("%f",&ak[i]);

std::sort(an,an+n);
std::sort(ak,ak+n);
int cn=0;
for(i=0,j=0;i<n;)//deceitfully
{
   if(an[i]>ak[j])
   {
       cn++;i++;j++;
   }
   else
   i++;
}
printf("Case #%d: %d ",k,cn);
c=0;
for(i=0,j=0;j<n;)//war
{
   if(an[i]<ak[j])
{
    c++;i++;j++;
}
else
            j++;

}
printf("%d\n",n-c);
    }
     return 0;

}
