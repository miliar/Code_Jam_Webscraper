#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

inline double timeLeft(double prod, double x) {
    return x / prod;
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int i, j;
    int T, NT;
    cin>>NT;
    double c, f, x;
    double t;
    double prod;
    for(T=1; T<=NT; ++T) {
        cin>>c>>f>>x;
        t = 0.0;
        prod = 2.0;
        while(1) {
            double t1 = timeLeft(prod, x);
            double t2 = timeLeft(prod, c) + timeLeft(prod+f, x);
            if (t1 < t2) {
                t += t1;
                break;
            } else {
                t += timeLeft(prod, c);
                prod += f;
            }
        }

        printf("Case #%d: %.9F\n", T, t);
    }
    return 0;
}
