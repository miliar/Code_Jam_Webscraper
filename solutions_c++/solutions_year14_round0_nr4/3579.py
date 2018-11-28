#include<cstdio>
#include<algorithm>
using namespace std;
float a[1005];
float ar[1005];
int main()
{
   freopen("D-large.in","r",stdin);
   freopen("out.txt","w",stdout);

 int g,i,j,t,q;
 scanf("%d",&t);
 for(q=0;q<t;q++)
 {
  scanf("%d",&g);
  for(i=0;i<g;i++)
   scanf("%f",&a[i]);
   for(i=0;i<g;i++)
    scanf("%f",&ar[i]);
  sort(a,a+g);
  reverse(a,a+g);
  sort(ar,ar+g);
  reverse(ar,ar+g);

  int k=0,l=g-1,count=0;
   j=0;
   while(j<=l)
   {
    if(a[j]>ar[k])
     {
       count++;
       k++;
       j++;
     }
    else if(a[j]<ar[k])
     {
       l--;
       k++;
     }
   }
   int count1=0;
   k=0;
   l=g-1;
   j=0;
   while(j<=l)
   {
      if(a[k]>ar[j])
      {
        count1++;
        k++;
        l--;
      }
      else if(a[k]<ar[j])
       {
           j++;
           k++;
       }
   }
   printf("Case #%d: %d %d\n",q+1,count,count1);
 }
 return 0;
}
