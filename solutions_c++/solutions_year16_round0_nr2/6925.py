#include <bits/stdc++.h>
using namespace std;

int func(char* s)
{
    int len = strlen(s);
    char pre = s[0];
    int i = 1, ans = 0;
    while (i < len)
    {
        if (s[i] == pre)
        {
            i++;
            continue;
        }

        if (pre == '-')
        {
            ans++;
            pre = '+';
        }else
        {
            ans++;
            pre = '-';
        }
        i++;
    }
    if (pre == '-')
        ans++;
    return ans;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    char panic[221];
	int T, n, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", panic);
        printf("Case #%d: %d\n", cas++, func(panic));
    }
	return 0;
}