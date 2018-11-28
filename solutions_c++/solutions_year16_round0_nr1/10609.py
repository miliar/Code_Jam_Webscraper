#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <cmath>
using namespace std;
bool b[10];
void run(long long x)
{
    long long y=x;
    while(y>0)
    {
        b[y%10]=true;
        y/=10;
    }
}
int len(long long x)
{
    long long y=x;
    int l=0;
    while(y>0)
    {
        y/=10;
        l++;
    }
    return l;
}
bool check()
{
    for (int k=0; k<10; k++)
    if (!b[k])
    {
        return false;
        break;
    }
    return true;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outl.txt", "w", stdout);
    int n;
    long long x;
    scanf("%d", &n);
    for (int i=1; i<=n; i++)
    {
        scanf("%lld", &x);
        int l=len(x);
        memset(b,false,sizeof(b));
        bool inso = true;
        //int j2=((double)pow(10,l+1))/x;
        //j2=max(j2,100);
        for (int j=1; j<=100; j++)
        {
            run(j*x);
            if (check())
            {
                printf("Case #%d: %lld\n", i, j*x);
                inso = false;
                break;
            }
        }
        if (inso)
        {
            /*for (int j=1; j<10; j++)
            {
                long long nxt=ceil((double)j*pow(10,l)/x)*x;
                run(nxt);
                if (check())
                {
                    printf("Case #%d: %lld\n", i, nxt);
                    inso = false;
                    break;
                }
            }*/
            if (inso)
            {
                printf("Case #%d: INSOMNIA\n", i);
            }
        }
    }
    return 0;
}
