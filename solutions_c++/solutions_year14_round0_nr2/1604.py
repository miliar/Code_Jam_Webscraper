#include <cstdio>
#include <algorithm>

double solve(){
    double c, f, x, sum_term = 0.0, ans = 100000.0;
    scanf("%lf %lf %lf", &c, &f, &x);
    for(int round = 0; round <= 100000; ++round){
        sum_term += 1.0 / (2.0 + round * f);
        ans = std::min(ans, c * sum_term + (x - c) / (2.0 + round * f));
    }
    return ans;
}

int main(){
    int allt;
    scanf("%d", &allt);
    for(int t = 1; t <= allt; ++t) printf("Case #%d: %.8lf\n", t, solve());
    return 0;
}

/*
c * (1/2 + 1/(2 + f) + 1/(2 + 2f) + ... + 1/(2 + nf)) + (x - c) * 1/(2 + nf)
*/