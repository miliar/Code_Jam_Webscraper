#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
double a[20]={0},b[20]={0};
int t,i,j,n,x=0,l,k,y=0,counter=0;

scanf("%d",&t);

for(i=1;i<=t;i++)
{
scanf("%d",&n);

for(j=0;j<n;j++)
scanf("%lf",&a[j]);

for(j=0;j<n;j++)
scanf("%lf",&b[j]);

sort(a,a+n);
sort(b,b+n);

/*for(j=0;j<n;j++)
printf("%lf ",a[j]);
printf("\n");

for(j=0;j<n;j++)
printf("%lf ",b[j]);

printf("\n");
*/

x=0;
counter=-1;
for(l=0;l<n;l++)
{
    for(j=counter+1;j<n;j++)
    {
        if(a[l]>b[j])
        {
            x++;
            counter=j;
           // printf("%d %d %d\n",x,l,j);
            break;

        }


    }
}
k=0;y=0;counter=-1;
for(l=0;l<n;l++)
{
   for(j=counter+1;j<n;j++)
   {
       if(a[l]<b[j])
       {
           y++;
           counter=j;
           break;
       }
   }
}
y=n-y;
printf("Case #%d: %d %d\n",i,x,y);

}

return 0;
}
