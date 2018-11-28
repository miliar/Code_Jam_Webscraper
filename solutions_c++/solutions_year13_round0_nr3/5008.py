#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int is_pal(long int n)
{
    long int temp = n;
    long int r, sum = 0;
    while(n)
    {
        r=n%10;
        n=n/10;
        sum=sum*10+r;
    }
    if(temp==sum)
        return 1;
    else
        return 0;
}

int main()
{
    int t, i;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        long long int a, b,l,h;
        int counter = 0,check1,check2;
        scanf("%lld%lld", &a, &b);
        l = (long int)ceil(sqrt(a));
        h = (long int)floor(sqrt(b));
        for(long int j=l; j<=h; j++)
        {
            check1 = is_pal(j);
            check2 = is_pal(j*j);
            if(check1==1 && check2==1)
                counter++;
        }
        printf("Case #%d: %d\n", i, counter);
    }
    return 0;
}
