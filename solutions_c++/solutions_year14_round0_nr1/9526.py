#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#define rep(i,a,b) for (int i = a; i <= b; ++i)
using namespace std;

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, cas(0);
    scanf("%d", &T);
    while (T--)
    {
        set<int> numSet;
        int row, sum(0), ans(-1);
        scanf("%d", &row);
        rep(i, 1, 4)
            rep(j, 1, 4)
            {
                int x;
                scanf("%d", &x);
                if (i == row)
                    numSet.insert(x);
            }
        scanf("%d", &row);
        rep(i, 1, 4)
            rep(j, 1, 4)
            {
                int x;
                scanf("%d", &x);
                if (i == row && numSet.count(x) != 0)
                    sum++, ans = x;
            }
        printf("Case #%d: ", ++cas);
        if (sum == 0)
            puts("Volunteer cheated!");
        else
        if (sum == 1)
            printf("%d\n", ans);
        else
            puts("Bad magician!");
    }

    return 0;
}
