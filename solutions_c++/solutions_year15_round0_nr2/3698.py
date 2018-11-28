#include <iostream>
#include <stdio.h>
using namespace std;

const int MaxN = 1005;

int T;
int n;
int p[MaxN];

int main()
{
    scanf("%d",&T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d",&n);
        for (int i = 0; i < n; ++i) {
            scanf("%d",&p[i]);
        }

        int result = 1000;
        for (int g = 1; g <= 1000; ++g) {

            int current = 0;
            for (int i = 0; i < n; ++i) {
                int d = p[i] / g;
                if ( p[i] % g == 0 ) d--;

                current += d;
            }

            result = min(result, current + g);
        }

        printf("Case #%d: %d\n",t,result);
    }

    return 0;
}
