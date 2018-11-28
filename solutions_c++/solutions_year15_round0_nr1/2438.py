#include <iostream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef long double ld;

int t,n;
char s[1005];

int main()
{
    /// freopen("input.txt", "r", stdin);
    /// freopen("output.txt", "w", stdout);

    scanf("%d",&t);
    for (int z = 0; z < t; ++z) {
        scanf("%d%s",&n,s);
        int cur = 0;
        int ans = 0;
        for (int i = 0; i <= n; ++i) {
            if (i > cur) { ans += i - cur; cur = i; }
            cur += s[i] - 48;
        }
        printf("Case #%d: %d\n", z+1, ans);
    }
    return 0;
}
