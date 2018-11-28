#include <iostream>
#include <cstdio>
#include <cstdio>
using namespace std;

#define maxn 1010

int n, cnt[maxn];
char s[maxn];

int main()
{
    freopen("A-large.in", "r", stdin);
//    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, ms, i, sum, ans, invite;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        ans = sum = 0;
        scanf("%d", &ms);
        scanf("%s", s);
        for(i = 0; i <= ms; i++)
            cnt[i] = s[i] - '0';
        for(i = 0; i <= ms; i++)
        {
            if(sum < i)
            {
                invite = i - sum;
                ans += invite;
            }
            else
                invite = 0;
            sum += cnt[i] + invite;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
