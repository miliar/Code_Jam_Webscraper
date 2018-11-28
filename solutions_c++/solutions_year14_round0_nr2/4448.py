#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

#define FI first
#define SE second
#define MP make_pair
#define PB push_back

const int MAXN = 100005;

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int main(){
    int tnum;
    scanf("%d", &tnum);
    for (int t=1; t<=tnum; t++){
        printf("Case #%d: ", t);
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double cps = 2.0, has = 0.0, time = 0;
        
        double ans = x/cps;
        
        if (c>=x){
            ans = x/cps;
        }
        else
            for (int i=1; time<ans; i++){
                double tgetf = c/cps;
                time += tgetf;
                cps += f;
                ans = min(ans, time + x/cps);
            }
        
        printf("%.7lf\n", ans);
    }
    return 0;
}
