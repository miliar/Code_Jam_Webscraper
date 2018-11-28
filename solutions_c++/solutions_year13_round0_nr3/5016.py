#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int pd(long int n)
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
        int counter = 0,checka,checkb;
        scanf("%lld%lld", &a, &b);
        l = (long int)ceil(sqrt(a));
        h = (long int)floor(sqrt(b));
        for(long int j=l; j<=h; j++)
        {
            checka = pd(j);
            checkb = pd(j*j);
            if(checka==1 && checkb==1)
                counter++;
        }
        printf("Case #%d: %d\n", i, counter);
    }
    return 0;
}
