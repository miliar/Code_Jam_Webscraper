#include<cstdio>
#include<algorithm>
using namespace std;
float arr[1005];
float ar1[1005];
int main()
{
   freopen("D-large.in","r",stdin);
   freopen("out.txt","w",stdout);

 int g,i,j,t,m;
 scanf("%d",&t);
 for(m=0;m<t;m++)
 {
  scanf("%d",&g);
  for(i=0;i<g;i++)
   scanf("%f",&arr[i]);
   for(i=0;i<g;i++)
    scanf("%f",&ar1[i]);
  sort(arr,arr+g);
  reverse(arr,arr+g);
  sort(ar1,ar1+g);
  reverse(ar1,ar1+g);

  int k=0,p=g-1,total=0;
   j=0;
   while(j<=p)
   {
    if(arr[j]>ar1[k])
     {
       total++;
       k++;
       j++;
     }
    else if(arr[j]<ar1[k])
     {
       p--;
       k++;
     }
   }
   int total1=0;
   k=0;
   p=g-1;
   j=0;
   while(j<=p)
   {
      if(arr[k]>ar1[j])
      {
        total1++;
        k++;
        p--;
      }
      else if(arr[k]<ar1[j])
       {
           j++;
           k++;
       }
   }
   printf("Case #%d: %d %d\n",m+1,total,total1);
 }
 return 0;
}
