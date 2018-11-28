#include<cstdio>
#include<algorithm>
using namespace std;
float arr[1005];
float ar[1005];
int main()
{
   freopen("D-large.in","r",stdin);
   freopen("output.txt","w",stdout);

 int n,i,j,test,q;
 scanf("%d",&test);
 for(q=0;q<test;q++)
 {
  scanf("%d",&n);
  for(i=0;i<n;i++)
   scanf("%f",&arr[i]);
   for(i=0;i<n;i++)
    scanf("%f",&ar[i]);
  sort(arr,arr+n);
  reverse(arr,arr+n);
  sort(ar,ar+n);
  reverse(ar,ar+n);

  int k=0,l=n-1,count=0;
   j=0;
   while(j<=l)
   {
    if(arr[j]>ar[k])
     {
       count++;
       k++;
       j++;
     }
    else if(arr[j]<ar[k])
     {
       l--;
       k++;
     }
   }
   int count1=0;
   k=0;
   l=n-1;
   j=0;
   while(j<=l)
   {
      if(arr[k]>ar[j])
      {
        count1++;
        k++;
        l--;
      }
      else if(arr[k]<ar[j])
       {
           j++;
           k++;
       }
   }
   printf("Case #%d: %d %d\n",q+1,count,count1);
 }
 return 0;
}
