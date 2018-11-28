#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int maxn = (int)1e6 + 10;

int n;
string c;

int main()
{
    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i)
    {
        cin >> c;
        int len = c.length(), ans = 0;
        for (int i = 1; i < len; ++i)
            if (c[i] != c[i - 1]) ++ans;
        if (c[len - 1] == '-') ++ans;
        printf("case #%d: %d\n", i + 1, ans);
    }
}