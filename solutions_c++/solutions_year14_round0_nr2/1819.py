
 #include <vector>
 #include <list>
 #include <map>
 #include <set>
 #include <deque>
 #include <queue>
 #include <stack>
 #include <bitset>
 #include <algorithm>
 #include <functional>
 #include <utility>
 #include <sstream>
 #include <iostream>
 #include <iomanip>
 #include <cstdio>
 #include <cmath>
 #include <fstream>
 #include <cstdlib>
 #include <ctime>
 #include <string>
 #include <cstring>
 using namespace std;

int main() {
    freopen("/Users/fengyelei/Desktop/in.in", "r", stdin);
    freopen("/Users/fengyelei/Desktop/out", "w", stdout);
    int T, t, i, j, k;
    scanf("%d", &T);
    for (t=1;t<=T;t++) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double ans = 0;
        double s = 2;
        while (1) {
            if (c/s+x/(s+f) < x/s) {
                ans += c/s;
                s+=f;
            }
            else {
                ans += x/s;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
