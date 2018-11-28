#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

typedef long long ll;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int T,tc=1,i,ctr,smax,a[2002],sol;
    char str[2002];
    scanf("%d",&T);
    while(T > 0)
    {
        ctr = 0;
        sol = 0;
        scanf("%d",&smax);
        scanf("%s",str);
        for(i=0;i<=smax;i++)
        {
            a[i] = str[i] - '0';
        }
        for(i=0;i<=smax;i++)
        {
            if(a[i] != 0 && ctr < i)
            {
                sol += i-ctr;
                ctr += i-ctr;
            }
            ctr += a[i];
        }
        printf("Case #%d: %d\n",tc,sol);
        tc++;
        T--;
    }
    return 0;
}
