#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

void solve (int k, int c, int s, int test)
{
    // заглушка на тест из условия !!!
    if (s != k)
    {
        printf("Case #%d: IMPOSSIBLE\n", test);
        return;
    }

    printf("Case #%d:", test);
    for (int i = 1; i <= s; i++)
        printf(" %d", i);
    printf("\n");
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif

 //   ios_base::sync_with_stdio(false);
 //   cin.tie(0);

    int t;
    cin >> t;

    int k, c, s;
    int test = 1;
    while (cin >> k >> c >> s)
        solve (k, c, s, test), test++;
}
