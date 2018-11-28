#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int a[110];
char str[110];

void flip(int l, int r)
{
    while (l <= r)
    {
        swap(a[l], a[r]);
        a[l]^=1;
        if (l != r) a[r]^=1;
        l++;r--;
    }
}

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++)
    {
        scanf("%s",str);
        int n = strlen(str);
        for (int i = 0; i < n; i++)
            if (str[i]=='+') a[i] = 1;
            else a[i] = 0;
        int ans = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (a[i] == 1) continue;
            if (a[0] == 0)
            {
                flip(0, i);
                ans++;
            }
            else
            {
                int j = 0;
                while (a[j] == 1) j++;
                flip(0, j);
                flip(0, i);
                ans+=2;
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
