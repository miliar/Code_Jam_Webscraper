#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long int t,ii;
    scanf("%lld",&t);
    for(ii=1;ii<=t;ii++)
    {
        long long int x,y,z;
        scanf("%lld",&x);
        scanf("%lld",&y);
        scanf("%lld",&z);
        long long int i,j,k,mi3=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<y;j++)
            {
                if((i&j)<z)
                    mi3++;
            }
        }
        printf("Case #%lld: %lld\n",ii,mi3);

    }
    return 0;
}
