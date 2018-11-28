#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, x, n, tmp, i;
    bool b[10];
    scanf("%d", &t);
    for(int y = 1; y <= t; y++){
        n = 0;
        memset(b, 1, sizeof b);
        n = 10;
        scanf("%d", &x);
        if(!x){printf("Case #%d: INSOMNIA\n", y); continue;}
        for(i = 1; n; i++){
            tmp = i * x;
            while(tmp){
                n -= b[tmp % 10];
                b[tmp % 10] = 0;
                tmp /= 10;
            }
        }
        printf("Case #%d: %d\n", y, (i - 1) * x);
    }
    return 0;
}
