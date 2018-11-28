#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int TTT;
    cin >> TTT;
    for(int T = 1; T <= TTT; ++T)
    {
        int c, d, v;
        cin >> c >> d >> v;
        vector<int> a(d);
        for(int i = 0; i < d; ++i)
            cin >> a[i];

        int ans = 0;

        if(c == 1)
        {
            vector<bool> can_be;
            can_be.assign(v+1, false);
            can_be[0] = true;
            for(int i = 0; i < d; ++i)
                for(int j = v; j >= 0; --j)
                    if(can_be[j])
                    {
                        int x = j + a[i];
                        if(x <= v)
                            can_be[x] = true;
                    }
            for(int i = 1; i <= v; ++i)
                if(!can_be[i])
                {
                    ++ans;
                    for(int j = v; j >= 0; --j)
                        if(can_be[j])
                        {
                            int x = j + i;
                            if(x <= v)
                                can_be[x] = true;
                        }
                }
        }


        cout << "Case #" << T << ": " << ans << endl;
    }

    return 0;
}
