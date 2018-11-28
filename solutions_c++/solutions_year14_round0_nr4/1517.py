#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
double a[1005],b[1005];
bool c[1005];
int main(){
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, n;
    cin >> T;
    for (int o = 1; o <= T; o++){
        cin >> n;
        for (int i = 0; i < n; i++)
            scanf("%lf", a + i);
        for (int i = 0; i < n; i++)
            scanf("%lf", b + i);
        sort(a, a + n, less<double>());

        sort(b, b + n, less<double>());
        int ans1 = 0, ans2 = 0;
        int i, s = 0, t = n - 1;
        for (i = 0; i < n; i ++){
            if (a[i] < b[s]) t--;
            else {s ++; ans1++;}
        }
        memset(c, 0, sizeof(c));
        for (int i = 0; i < n; i++){
            bool OK = 1;
            for (int j = 0; j < n; j++)
                if (!c[j] && b[j] > a[i]){
                    c[j] = 1; OK = 0; break;
                }
            if (OK) ans2++;
        }
        printf("Case #%d: %d %d\n", o, ans1, ans2);
    }
}
