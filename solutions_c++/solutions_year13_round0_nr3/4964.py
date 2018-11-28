#include<iostream>
using namespace std;
#include<cmath>
#include<cstdio>

int main()
{
    freopen("C-small-attempt6.in","r",stdin);
    freopen("output.txt","w",stdout);
    int arr[]={1,4,9,121,484};
    int t,x;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
                    int a,b,i,count=0;
                    scanf("%d %d",&a,&b);
                    for(i=0;i<5;i++)
                    {
                                    if(arr[i]>=a&&arr[i]<=b)
                                      count++;
                    }
                    printf("Case #%d: %d\n",x+1,count);
    }
} 
