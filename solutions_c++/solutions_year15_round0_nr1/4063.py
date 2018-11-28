#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

char s[1010];
int n;
int cnt;
int ans;

int dig(char ch)
{
    return ch-'0';
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cns = 1; cns <= t; cns++)
    {
        cin >> n >> s;
        cnt = dig(s[0]);
        ans = 0;
        for(int i = 1; i <= n; i++)
        {
            if(i > cnt)
            {
                ans += i-cnt;
                cnt = i;
            }
            cnt += dig(s[i]);
        }
        cout << "Case #" << cns << ": " << ans << endl;
    }
    return 0;
}
