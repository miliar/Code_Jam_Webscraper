#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for (int i = 0; i < len; i++) cerr << arr[i] << " "; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for (const auto &e : it) cerr << e << " "; cerr << endl;}
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0
#define print_iterable(it) (void)0
#endif

typedef long long ll;
const int N = 1005;

int n, k;
char s[N];

void flip(char &c)
{
    c = c == '+' ? '-' : '+';
}

void solve()
{
    scanf("%s%d", s, &k);
    n = strlen(s);

    int cnt = 0;
    for (int i = 0; i + k <= n; i++)
        if (s[i] == '-')
        {
            cnt++;
            for (int j = 0; j < k; j++)
                flip(s[i + j]);
        }

    for (int i = 0; i < n; i++)
        if (s[i] == '-')
        {
            puts("IMPOSSIBLE");
            return;
        }
    printf("%d\n", cnt);
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("\n\ntime = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
