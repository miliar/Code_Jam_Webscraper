#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int abs(int x)
{
    return x < 0? -x:x;
}
int main()
{
    freopen("/Users/os/Desktop/A-small-attempt1.in", "r", stdin);
    freopen("/Users/os/Desktop/A-small-attempt1.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for (int cases = 1; cases <= t;cases++)
    {
        int n;
        char a[105],b[105];
        scanf("%d",&n);
        scanf("%s",a);
        scanf("%s",b);
        int ans = 0;
        int la = (int)strlen(a),lb = (int)strlen(b);
        int p = 0,q= 0;
        while (p < la || q < lb)
        {
            if (a[p] != b[q]) {ans = -1;break;}
            int i,j;
            for (i = 0; i < la - p; i++)
                if (a[p+i] != a[p]) break;
            for (j = 0; j < lb - q; j++)
                if (b[q+j] != b[q]) break;
            ans += abs(i-j);
            p += i;
            q += j;
        }
        if (ans <0) printf("Case #%d: Fegla Won\n",cases);
        else printf("Case #%d: %d\n",cases,ans);
    }
}