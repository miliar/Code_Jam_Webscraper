#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
for(int l=1;l<=t;l++)
{
    int n;
    scanf("%d",&n);
    double a[1002];
    double b[1002];
    for(int i=0;i<n;i++)
        scanf("%lf",&a[i]);
    for(int i=0;i<n;i++)
        scanf("%lf",&b[i]);
    sort(a,a+n);
    sort(b,b+n);
    int i=0,j=0;
    int count=0,ans1=0;
    while(count<n)
    {
        if(a[i]<b[j])
            i++;
        else
        {
            i++;
            j++;
            ans1++;
        }
        count++;
    }

    int ans2=0;
    i=0,j=0;
    count=0;
    for(i=0;i<n;i++)
    for(j=0;j<n;j++)
    if(b[j]>a[i]){
    ans2++;
    b[j]=0;
    break;}

    ans2=n-ans2;





    printf("Case #%d: %d %d\n",l,ans1,ans2);





}



return 0;}
