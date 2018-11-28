#include <bits/stdc++.h>

using namespace std;
const int N = 105;
int n;
long double V, T, r[N], t[N];
void testCase() {
    scanf("%d %Lf %Lf", &n, &V, &T);
    for(int i = 1; i <= n; i++) {
        scanf("%Lf %Lf", &r[i], &t[i]);
    }
    if(n == 1) {
        if(T != t[1]) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%Lf\n", V / r[1]);
        }
    } else {
        if(t[1] == t[2]) {
            if(T != t[1]) {
                printf("IMPOSSIBLE\n");
            } else {
                printf("%Lf\n", V / (r[1] + r[2]));
            }
        } else {
            if(T > max(t[1], t[2]) || T < min(t[1], t[2])) {
                printf("IMPOSSIBLE\n");
                return;
            }
            long double V2 = /*min(V,*/ V * (T - t[1]) / (t[2] - t[1]);
            long double V1 = V - V2;
            long double time1 = V2 / r[2];
            long double time2 = V1 / r[1];
//             printf("Pomocniczo V %Lf %Lf\n", V1, V2);
//             printf("Pomocniczo %Lf %Lf\n", time2, time1);
            printf("%.9Lf\n", max(time1, time2));
        }
    }
}

int main() {
    int t;
    scanf("%d" ,&t);
    for(int test = 1; test <= t; test++) {
        printf("Case #%d: ", test);
        testCase();
    }
    return 0;
}