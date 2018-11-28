#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef pair<int, int> ii;

void solve_testcase()
{
    int n, x;
    scanf("%d%d", &n, &x);
    int s[n];
    for (int i = 0; i < n; ++i)
        scanf("%d", s+i);
    sort(s, s+n);

    int nice = 0;
    for (int l = 0, r = n-1; ; ) {
        while (r > l && s[l] + s[r] > x) --r;
        if (r > l && s[l] + s[r] <= x) {
            ++l,
            --r;
            ++nice;
        }
        else break;
    }
    printf("%d\n", n-nice);
}

int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w+", stdout);
    #endif

    int testcases_count;
    scanf("%d", &testcases_count);
    for (int testcase = 1; testcase <= testcases_count; ++testcase) {
        printf("Case #%d:", testcase);
        putchar(' ');
        //putchar('\n');
        solve_testcase();
    }
}
