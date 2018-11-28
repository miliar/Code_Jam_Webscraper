#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int M = 10100;
int a[M];
int n;

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int t=1; t<=test; t++)
    {
        scanf("%d", &n);
        int x = 0;
        int y = 0;
        int my = 0;
        for(int i=1; i<=n; i++)
        {
            scanf("%d", &a[i]);
            if(i>1)
            {
                if(a[i-1]-a[i]>0)
                    x += a[i-1]-a[i];
                my = max(my, a[i-1]-a[i]);
            }
        }
        for(int i=1; i<n; i++)
        {
            y += min(a[i], my);
        }
        printf("Case #%d: %d %d\n", t, x, y);
    }
    return 0;
}
