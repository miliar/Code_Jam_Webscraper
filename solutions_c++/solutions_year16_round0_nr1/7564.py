#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
bool v[10];
int cal(int x)
{
    int s = 0;
    while (x)
    {
        if (v[x % 10] == false)
        {
            v[x % 10] = true;
            s++;
        }
        x /= 10;
    }
    return s;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, Case = 0;
    scanf("%d", &t);
    while (t--)
    {
        memset(v, false, sizeof(v));
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", ++Case);
            continue;
        }
        int now = n, m = 0;
        while (1)
        {
            m += cal(now);
            if (m == 10)
                break;
            now += n;
        }
        printf("Case #%d: %d\n", ++Case, now);
    }
    
}