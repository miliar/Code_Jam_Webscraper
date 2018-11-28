#include<iostream>
using namespace std;
#include<stdio.h>
char a[1005];
int n, Smax, b[1005], neng, ans;
int i, j;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &n);
    for(i = 0; i < n; i++)
    {
        scanf("%d ", &Smax);
        neng = 0;
        ans = 0;
        for(j = 0; j <= Smax; j++)
        {
            scanf("%c", &a[j]);

            b[j] = a[j] - '0';
            if(j == neng && b[j] == 0)
            {
                ans ++;
                neng ++;
            }
            if(b[j] > 0 || j < neng)
            {
                neng += b[j];
            }
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}
