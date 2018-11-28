// *CoDeD by Ye.A
# include <iostream>
# include <cstdlib>
# include <cstdio>
# include <cmath>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <stack>
# include <algorithm>
# include <set>
# include <map>

# define task "A-large"
# define FOR(x, y, z) for(int x = y; x <= z; x++)
# define FRO(x, y, z) for(int x = y; x >= z; x--)

typedef long long ll;
using namespace std;

const int MAXN = (int) 1e5 + 5;
const int INF = (int) 0x7fffffff;
const int MOD = (int) 1e9 + 7;

int main () {
        freopen (task".in", "r", stdin);
        freopen (task".out", "w", stdout);

    int T;
    scanf("%d", &T);
    FOR(test, 1, T) {
        int n, cnt = 0, ans = 0;
        scanf("%d", &n);
        string s;
        cin >> s;
        FOR(i, 0, s.size() - 1){
            if(cnt < i)
                ans += i - cnt,
                cnt = i;
            cnt += s[i] - '0';
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
