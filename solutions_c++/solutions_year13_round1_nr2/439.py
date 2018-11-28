#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<set>
#include<string.h>
#include<algorithm>
using namespace std;
int e,r,n,maxi=0;
int arr[20];
void find(int pos,int sum,int ener)
{
   ener=ener+r;
   if(ener>e) return;
   if(pos==n-1)
   {
      sum=sum+ener*arr[pos];
      if(sum>maxi) maxi=sum;
      return;
   }
   int i;
   for(i=0;i<=ener;i++)
      find(pos+1,sum+i*arr[pos],ener-i);
   return;
}
int main()
{
    freopen("reada.txt","r",stdin);
    freopen("outa.txt","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&e,&r,&n);
        for(j=0;j<n;j++)
           scanf("%d",&arr[j]);
        maxi=0;
        find(0,0,e-r);
        printf("Case #%d: %d\n",i,maxi);
    }
    return 0;
}
