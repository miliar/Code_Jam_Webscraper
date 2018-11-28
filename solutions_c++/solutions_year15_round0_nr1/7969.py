#include <cstdio>

using namespace std;

const int N = 1010;
int n;
char s[N];

void solve(int g)
{
    scanf("%d %s", &n, s);
    int k = s[0] - '0', z = 0;
    for (int i = 1; i <= n; i++)
    {
        int x = s[i] - '0';
        if (i > k)
        {
            int t = i - k;
            z += t;
            k += x + t;
        } else
        k += x;
    }
    printf("Case #%d: %d\n", g, z);
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
