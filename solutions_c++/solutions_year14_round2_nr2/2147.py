#include <iostream>
#include <stdio.h>

using namespace std;

long long int nr;
int a, b, k;

void sol()
{
    int c;
    for (int i=0; i<a; i++)
        for (int j=0; j<b; j++)
        {
            c=i&j;
            if (c<k)
                nr++;
        }
}

int main()
{
    freopen("lot.in", "r", stdin);
    freopen("lot.out", "w", stdout);
    ///Case #1: 10
    int T;
    scanf("%d", &T);
    for (int r=1; r<=T; r++)
    {
        printf("Case #%d: ", r);
        scanf("%d %d %d", &a, &b, &k);
        nr=0;
        sol();
        printf("%d\n", nr);
    }
    return 0;
}
