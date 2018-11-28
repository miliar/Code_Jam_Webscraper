#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 1000000000
#define eps 1e-8
#define lld long long
#define mem(a,b) memset((a),(b),sizeof((a)))
using namespace std;
double c,f,x;
double last;
double cal(int t) {
    if (t == 0) return x / 2.0;
    double p = last + c / (2.0 + (t - 1) * f);
    last = p;
    return p + x / (2.0 + t * f);
}
int main() {
    int T,i,cas=0;   freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--) {

        cin>>c>>f>>x;
        i=0;
        last = 0;
        double best = 1e20;
        while(1) {
            double now = cal(i);
            if (now < best) best = now;
            else break;

            i++;
        }
        printf("Case #%d: %.7lf\n", ++cas, best);
    }
     fclose(stdin);
    fclose(stdout);
    return 0;
}
