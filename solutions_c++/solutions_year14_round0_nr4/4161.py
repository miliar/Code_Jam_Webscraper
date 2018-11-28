#include <iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>

using namespace std;

void deceitwar(int t);
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
        deceitwar(i);
    return 0;
}
void deceitwar(int t)
{
    int n;
    int i,j;
    scanf("%d",&n);
    size_t nsize = n;
    double a[1010]={};
    double b[1010]={};
    for(i=0;i<n;i++)
        scanf("%lf",&a[i]);
    for(i=0;i<n;i++)
        scanf("%lf",&b[i]);

    std::sort(a,a+nsize);
    std::sort(b,b+nsize);
    int s=0;
    int e=n;
    int c=0;
    for(i=0;i<n;i++)
    {
        if(a[i]<b[s])
        {
            e=e-1;
        }
        else
        {
            s=s+1;
            c++;
        }
    }

    i=0;
    j=0;
    while((i<n)&&(j<n))
    {
        if(a[i]<b[j])
        {
            i++;
            j++;
        }
        else
        {
            j++;
        }
    }
    printf("Case #%d: %d %d\n",++t,c,n-i);
}
