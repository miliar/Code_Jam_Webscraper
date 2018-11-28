#include <bits/stdc++.h>
using namespace std;
const int N=1e3+5;
int p[N];
int n;

int main()
{
    int t;
    scanf("%d", &t);
    for(int it=1; it<=t; ++it)
    {
        memset(p, 0, N*sizeof(int));
        scanf("%d", &n);
        for(int i=0; i<n; ++i) scanf("%d", &p[i]);
        int mn=1e9;
        for(int i=1; i<=1000; ++i)
        {
            int cnt=0;
            for(int j=0; j<n; ++j) cnt+=(p[j]-1)/i;
            mn=min(mn, i+cnt);
        }
        printf("Case #%d: %d\n", it, mn);
    }
    return 0;
}
