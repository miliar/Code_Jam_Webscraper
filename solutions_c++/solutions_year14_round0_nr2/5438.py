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

void run()
{
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);

    long double rate = 2;
    long double elapsed_time = 0;
    long double last_time = x / rate;
    for (;;) {
        elapsed_time += c / rate;
        rate += f;
        long double new_time = elapsed_time + x / rate;
        if (new_time > last_time) {
            break;
        } else {
            last_time = new_time;
        }
    }
    printf("%.7lf\n", (double) last_time);
}

int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("B-small.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w+", stdout);
    #endif

    int testcases;
    scanf("%d", &testcases);
    for (int test = 1; test <= testcases; ++test) {
        printf("Case #%d: ", test);
        run();
    }

    return 0;
}
