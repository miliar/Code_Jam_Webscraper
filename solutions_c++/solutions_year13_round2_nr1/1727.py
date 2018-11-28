#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A_out.txt", "w", stdout);

    int t, x, n, i, y, ins, parc;
    long long a, v[100];
    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%I64d %d", &a, &n);
        for(i = 0; i < n; i++) {
            scanf("%I64d", &v[i]);
        }
        sort(v, v+n);
        y = n;
        ins = 0;
        i = 0;

        if(a > 1) {
            while(i < n) {
                while(i < n && a > v[i]) {
                    a = a+v[i];
                    i++;
                }

                parc = ins + n-i;
                if(parc < y) y = parc;
                a = 2*a-1;
                ins++;
            }
        }
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
