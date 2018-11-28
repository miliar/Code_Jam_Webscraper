#include <bits\stdc++.h>
using namespace std;
const int N = 105;
int T;
int n;
double v, x;
double r[N], c[N];
int main()
{
    freopen("B-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(int qw = 1; qw <= T; ++qw){
        cin >> n >> v >> x;
        for(int i = 0; i < n; ++i){
            cin >> r[i] >> c[i];
        }
        double ans = 0;
        if(n == 1){
            if(c[0] == x){
                ans = v / (r[0]);
                printf("Case #%d: %.9f\n", qw, ans);
            }
            else{
                printf("Case #%d: IMPOSSIBLE\n", qw);
            }
            continue;
        }
        int flag = 1;
        if(c[0] > x && c[1] > x){
            flag = 0;
        }
        if(c[0] < x && c[1] < x){
            flag = 0;
        }
        if(flag && c[0] == c[1]){
            ans = v / (r[0] + r[1]);
            printf("Case #%d: %.9f\n", qw, ans);
            continue;
        }
        if(!flag){
            printf("Case #%d: IMPOSSIBLE\n", qw);
        }
        else{
            double b = v * (x - c[0]) / (c[1] - c[0]);
            double a = v - b;
            double t1 = a / (r[0]);
            double t2 = b / (r[1]);
            printf("Case #%d: %.9f\n", qw, max(t1, t2));
        }
    }
    return 0;
}
