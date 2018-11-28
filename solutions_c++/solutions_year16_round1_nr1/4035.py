#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
#define N 1005
char a[N];

void solve()
{
    scanf("%s", a);
    string s = "";
    s += a[0];
    int n = strlen(a);
    for (int i = 1; i < n; ++i)
        if (s + a[i] > a[i] + s)
            s = s + a[i];
        else
            s = a[i] + s;
    cout << s << endl;
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}