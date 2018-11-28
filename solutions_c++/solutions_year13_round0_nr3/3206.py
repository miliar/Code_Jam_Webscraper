#include<cstdio>
#include<iostream.h>
int main()
{
    freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
    int arr[5]={1,4,9,121,484};
    int t,i,j,c,a,b;
    scanf("%d",&t);
    for(j=0;j<t;j++)
    {
         scanf("%d %d",&a,&b);
         c=0;
         for(i=0;i<5;i++)
         {
              if(arr[i]>=a&&arr[i]<=b)
                  c++;
         }
         printf("Case #%d: %d\n",j+1,c);
    }
}
         
