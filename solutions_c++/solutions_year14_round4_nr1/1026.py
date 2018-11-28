#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int ary[10020], vis[100020];

int main()
{
    freopen("2a.in", "r", stdin);
    freopen("2a.out",  "w", stdout);
    int T, n, x;
    cin>>T;
    for(int tt = 1; tt <= T; ++tt)
    {
        cin>>n>>x;
        for(int i = 0; i <n; ++i)
            cin>>ary[i];
        sort(ary, ary + n);
        memset(vis, 0, sizeof(vis));
        int ed = n - 1;
        int ans = 0;
        for(int i = 0; i < n; ++i)
        {
            if(vis[i])
                continue;
            while(ed > i)
            {
                if(ary[i] + ary[ed] <= x)
                {
                    vis[ed--] = 1;
                    break;
                }
                ed--;
            }
            ++ans;
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
