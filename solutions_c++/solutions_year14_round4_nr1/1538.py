#include <algorithm>
#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int ncases;
    scanf("%d", &ncases);
    for (int qq = 1; qq <= ncases; ++qq)
    {
        int t, x;
        scanf("%d %d", &t, &x);
        vector<int> ss(t);
        for (auto& s: ss) scanf("%d", &s);
        sort(begin(ss), end(ss));
        reverse(begin(ss), end(ss));

        auto l = begin(ss), r = end(ss) - 1;
        int cnt = 0;

        while (l <= r)
        {
            int t = *l++;
            if (t + *r <= x) --r;
            ++cnt;
        }

        printf("Case #%d: %d\n", qq, cnt);
    }

    return 0;
}

