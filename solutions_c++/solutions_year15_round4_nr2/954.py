#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define rep(I,N) for(int (I) = 0; (I) < (N); (I)++)

typedef pair<int,int> pii;
typedef long long ll;

#define MAXN 107
int n;
double w_v, w_t;
double rate[MAXN], temp[MAXN];
double check(double v1, double t1){
    if (v1 > w_v) return -1.0;
    double needed = (w_v - v1);
    if (needed < 1e-8){
        if (abs(t1 - w_t) < 1e-8)
            return 0.0;
    }
    double new_temp = (v1 * t1 + needed * temp[1]) / (v1 + needed);
    if (abs(new_temp - w_t) < 1e-8){
        return needed / rate[1];
    }
    return -1.0;
}
vector<double> solutions;
int main(){
    int t;
    scanf("%d",&t);
    rep(testId,t){
        printf("Case #%d: ", testId+1);
        scanf("%d%lf%lf",&n, &w_v, &w_t);
        rep(i, n){
            scanf("%lf%lf",&rate[i], &temp[i]);
        }
        if (n == 1){
            if (abs(w_t - temp[0]) > 1e-8){
                printf("IMPOSSIBLE\n");
                continue;
            }
            printf("%.7lf\n", w_v / rate[0]);
            continue;
        }

        solutions.clear();
        bool both = false;
        bool can = false;
        if (abs(w_t - temp[0]) < 1e-8){
            both = true;
            solutions.push_back(w_v / rate[0]);
        }
        if (abs(w_t - temp[1]) < 1e-8){
            if (both)
                can = true;
            solutions.push_back(w_v / rate[1]);
        }
        if (abs(temp[0] - temp[1]) > 1e-8){
            double v2 = (w_v * (w_t - temp[0])) / (temp[1] - temp[0]);
            if (v2 > 0.0){
                double v1 = w_v - v2;
                if (v1 > 0.0){
                    solutions.push_back(max(v1 / rate[0], v2/rate[1]));
                }
            }
        }
        if (can){
            solutions.push_back(w_v / (rate[0] + rate[1]));
        }
        if (!solutions.size()){
            printf("IMPOSSIBLE\n");
            continue;
        }
        double my_s = 1e20;
        for(int i = 0; i < solutions.size(); i++){
            my_s = min(my_s, solutions[i]);
        }
        printf("%.7lf\n", my_s);
    }
}
