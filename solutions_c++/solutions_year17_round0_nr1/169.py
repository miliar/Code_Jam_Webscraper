#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const int N = 1010;
int n, k;
char s[N];
bool a[N];

void solve()
{
    scanf(" %s %d ", s, &k);
    n = strlen(s);
    for (int i = 0; i < n; i++)
        a[i] = (s[i] == '-');
    int ans = 0;
    for (int i = 0; i + k <= n; i++)
    {
        if (!a[i]) continue;
        for (int j = 0; j < k; j++)
            a[i + j] ^= 1;
        ans++;
    }
    for (int i = 0; i < n; i++)
        if (a[i])
        {
            printf("IMPOSSIBLE\n");
            return;
        }
    printf("%d\n", ans);
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}
