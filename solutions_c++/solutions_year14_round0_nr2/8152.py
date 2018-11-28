#include<iostream>
#include<iomanip>
using namespace std;
double pre[200001];

double solve(double c, double f, double x){
    double best = x / 2.0;
    for(int i = 0; i < 150000; ++i) {
        double cand = c * pre[i] + x / (2.0 + f * i);
        best = min(best, cand);
    }
    return best;
}

int main(){
    double c, f, x;

    int T;
    cin >> T;
    pre[0] = 0;

    for(int t = 1; t <= T; ++t) {
        cin >> c >> f >> x;
        for(int i = 1; i <= 200000; ++i)
            pre[i] = pre[i - 1] + 1.0 / (2.0 + f * (i - 1));
        cout << "Case #" << t << ": " << fixed << setprecision(7) << solve(c, f, x) << endl;
    }
    return 0;
}
