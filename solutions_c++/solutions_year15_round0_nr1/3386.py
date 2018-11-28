#include <bits/stdc++.h>
using namespace std;
#define FOR(i, s, t) for(int i = s, _t = t; i < _t; i++)

const int maxn = 1000 + 5;
int n;
char s[maxn];

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int kase;
    scanf("%d", &kase);
    FOR(T, 1, kase + 1)
    {
        scanf("%d%s", &n, s);
        int ans = 0, sum = 0;

        FOR(i, 0, n+1)
        {
            if(sum < i)
            {
                ans += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }

        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
