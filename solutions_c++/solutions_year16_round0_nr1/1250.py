#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

void solve (int n, int test)
{
 //   cerr << "n = " << n << endl;
    if (n == 0)
    {
        printf("Case #%d: INSOMNIA\n", test);
        return;
    }

    int is_was = 0;
    const int target = (1 << 10) - 1;

    for (int i = 1;; i++)
    {
        ll x = n * (ll)i;
        while (x > 0)
            is_was |= (1 << (x % 10)), x /= 10;
        if (is_was == target)
        {
            printf("Case #%d: %lld\n", test, n * (ll)i);
            return;
        }
    }
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

    int n;
    int test = 1;
    while (cin >> n)
        solve (n, test), test++;
}
