#include <iostream>
#include <cstdio>
#define eps 10e-8
using namespace std;
double C, F, X;

double calc(int x){
    int cnt = 0;
    double tot = 0;
    double out = 2;
    double ans = 0;
    while (cnt < x){
        ans += C / out;
        out += F;
        cnt ++;
    }
    ans += X / out;
    return ans;
}

double solve(){
   // cout << C << " " << F << " " << X << endl;
    double ans = X;
    for (int i = 0; i <= X; ++i){
        double tmp = calc(i);
        //cout << tmp << endl;
        if (tmp - eps < ans){
            ans = tmp;
        }
        else{
            return ans;
        }
    }
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int _;
    scanf("%d", &_);
    for (int __ = 1; __ <= _; ++__){
        printf("Case #%d: ",__);
        scanf("%lf%lf%lf", &C, &F, &X);
        double  ans = solve();
        printf("%.6lf\n", ans);
    }
    return 0;
}
