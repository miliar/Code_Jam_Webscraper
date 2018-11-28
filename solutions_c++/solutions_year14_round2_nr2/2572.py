#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("outsmallB.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        int a,b,k;
        scanf("%d %d %d", &a, &b, &k);
        int min1=(a<k)?a:k;
        int min2=(min1<b)?min1:b;
        int ctr=0;
        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                for(int m=0; m<k; m++)
                {
                    if((i&j)==m)
                    {
                        ctr++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", tt, ctr);
    }
    return 0;
}
