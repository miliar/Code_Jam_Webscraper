#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    scanf("%d", &t);
    for(int j=1; j<=t; ++j)
    {
        int smax, sum=0, mx=0;
        char c;
        scanf("%d ", &smax);
        for(int i=0; i<smax; ++i)
        {
            scanf("%c", &c);
            sum+=c-'0';
            mx=max(mx, i+1-sum);
        }
        scanf("%c", &c);
        printf("Case #%d: %d\n", j, mx);
    }
    return 0;
}
