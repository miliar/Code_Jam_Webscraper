#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
using namespace std;
typedef long long lng;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        int R, C, W;
        cin >> R >> C >> W;
        int a = C%W;
        if(a == 0)
        {
            cout << ((C/W)*(R-1))+(C/W) + (W - 1) << endl;
        }
        else
        {
            cout << ((C/W)*(R-1))+( C/W) + (W) << endl;
        }
        //int ans =
        //cout << (R * C) - ()
    }
    return 0;
}
