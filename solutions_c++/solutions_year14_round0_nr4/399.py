#include<iostream>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

const int N = 1010;

double a[N], b[N];
bool v[N];

int main() {
//    freopen("D1.in", "r", stdin);
//    freopen("D1.out", "w", stdout);
    int t, n; scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) scanf("%lf", &a[i]);
        for(int i = 0; i < n; ++i) scanf("%lf", &b[i]);

        sort(a, a+n); sort(b, b+n);

        int la = 0, ra = n - 1, lb = 0, rb = n - 1;
        int y = 0, z = 0;

        memset(v, false, sizeof(v));
        for(int i = 0; i < n; ++i) {
            int f = 1;
            for(int j = 0; j < n; ++j) {
                if(!v[j] && b[j] > a[i]) {
                    v[j] = true; f = 0;
                    break;
                }
            }
            z += f;
        }

        while(la <= ra) {
            if(a[la] > b[lb]) {
                y++;
                la++, lb++;
            }
            else {
                la++, rb--;
            }
        }

        printf("Case #%d: %d %d\n", cas, y, z);

    }
    return 0;
}
