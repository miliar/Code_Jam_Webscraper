#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

set<int> st;
set<int>::iterator it;

vector<int> ans;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double t = 1e9, nt = 0, nf = 2.0;
        for(int i = 0; i <= 2000; i++) {
            nt = 0.0;
            nf = 2.0;
            for(int j = 0; j < i; j++) {
                nt += c / nf;
                nf += f;
            }
            nt += x / nf;
            t = min(t, nt);
        }
        printf("Case #%d: %.7f\n", cnt++, t);
    }

    return 0;
}
