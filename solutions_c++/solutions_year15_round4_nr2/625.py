#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <deque>

using namespace std;

int N, M, K, T;
int X, C;
int v_speed[128];
int r_speed[128];

int run()
{
    int v = 0;
    int a, b, c, d;
    scanf("%d%d.%d%d.%d", &N, &a, &b, &c, &d);
    //cin >> N >> X >> C;
    X = a * 10000 + b;
    C = c * 10000 + d;
    for(int i = 0; i < N; ++i) {
        scanf("%d.%d%d.%d", &a, &b, &c, &d);
        //cin >> v_speed[i] >> r_speed[i];
        v_speed[i] = a * 10000 + b;
        r_speed[i] = c * 10000 + d;
        if(r_speed[i] == C) {
            v += v_speed[i];
        }
    }
    double res = X;
    if(v > 0) {
        res /= v;
        printf("%.09lf\n", res);
        return 0;
    }
    if(N == 1) {
        printf("IMPOSSIBLE\n");
        return 0;
    }
    
    if((r_speed[0] > C && r_speed[1] > C) || (r_speed[0] < C && r_speed[1] < C)) {
        printf("IMPOSSIBLE\n");
        return 0;
    }

    int gong_0 = r_speed[0] - C;
    int gong_1 = r_speed[1] - C;
    if(gong_0 < 0) {
        gong_0 = -gong_0;
    }
    if(gong_1 < 0) {
        gong_1 = -gong_1;
    }
    double time_0 = res * gong_1 / (gong_0 + gong_1) / v_speed[0];
    double time_1 = res * gong_0 / (gong_0 + gong_1) / v_speed[1];

    printf("%.09lf\n", max(time_1, time_0));
    return 0;
}

int main()
{
    scanf("%d", &T);
    for(int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}


