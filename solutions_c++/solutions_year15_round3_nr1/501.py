#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output-large.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int TTT;
    cin >> TTT;
    for(int T = 1; T <= TTT; ++T)
    {
        int R, C, W;
        cin >> R >> C >> W;

        int ans = C / W;
        ans *= R - 1;

        int ans2 = 0;
        for(int i = W; i <= C; i += W)
        {
            int cur = i / W;
            cur += W-1;
            if( i > 1 )
                if( i <= C - 1)
                    ++cur;
            ans2 = max(ans2, cur);
        }
        ans += ans2;

//        ans += W - 1;
//        if((C % W) != 0)
//            ++ans;
//        if((C / W) > 1)
//            ++ans;

        cout << "Case #" << T << ": " << ans << endl;
    }

    return 0;
}
