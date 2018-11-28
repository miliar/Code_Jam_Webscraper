#include<iostream>
#include<cstdio>

using namespace std;

const int maxn = 1010;
int T, n;
char s[maxn];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for(int cas = 1; cas <= T; ++cas)
    {
        cin >> n >> s;
        int ans = 0;
        int cur = 0;
        for(int i = 0; s[i]; ++i)
        {
            int tmp = s[i] - '0';
            if (cur < i)
            {
                ans += i - cur;
                cur = i + tmp;
            }
            else
                cur += tmp;
        }

        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
