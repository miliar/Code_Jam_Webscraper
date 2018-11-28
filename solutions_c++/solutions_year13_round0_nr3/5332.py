#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int arr[] = {1,4,9,121,484,10201,12321,14641,40804,44944,
1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,
125686521,400080004,404090404};

int fnd(long n)
{
    for(int i=0;i<21;i++)
        if(arr[i]==n)
            return 1;
    return 0;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        long a,b,c=0;
        scanf("%ld%ld",&a,&b);
        for(long ii=a;ii<=b;ii++)
            if(fnd(ii)) c++;
        printf("Case #%d: %d\n",i,c);
    }
    return 0;
}
