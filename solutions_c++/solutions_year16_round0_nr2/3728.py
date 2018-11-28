#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char s[128];
int nr;

void solve()
{
    strcat(s, "+");
    nr = 0;
    char last = s[0];
    int n = strlen(s);

    for(int i = 1; i < n; i++)
        if(s[i] != last)
    {
        last = s[i];
        nr++;
    }
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T;
    scanf("%d\n", &T);
    for(int q = 1; q <= T; q++)
    {
        printf("Case #%d: ", q);
        gets(s);
        solve();
        printf("%d\n", nr);
    }

    return 0;
}
