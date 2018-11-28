#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void Fpre() {
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
}

int mp[5][5];
int a[5];
int main() {
    Fpre();
    int T;
    double C, F, X;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%lf%lf%lf", &C, &F, &X);
        double per = 2.0;
        double tim = 0;
        while (X/(per+F)+C/per <= X/per) {
            tim += C / per;
            per += F;
        }
        tim += X / per;
        printf("Case #%d: %.7f\n", cas, tim);
    }
    return 0;
}
