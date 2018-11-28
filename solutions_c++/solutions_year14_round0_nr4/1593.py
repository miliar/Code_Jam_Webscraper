
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

double a[1000], b[1000];
int n;

int f() {
    int i, j, k;
    bool v[1000];
    k = 0;
    memset(v, 0, sizeof(v));
    for (i=0; i<n; i++) {
        for (j=0; j<n; j++) {
            if (!v[j]&&b[j]<a[i]) {
                k++, v[j]=1;
                break;
            }
        }
    }
    return k;
}

int g() {
    int i, j, k;
    bool v[1000];
    k = 0;
    memset(v, 0, sizeof(v));
    for (i=0; i<n; i++) {
        for (j=0; j<n; j++) {
            if (!v[j]&&b[j]>a[i]) {
                k++, v[j]=1;
                break;
            }
        }
    }
    return n-k;
}

int main() {
    freopen("/Users/fengyelei/Desktop/in.in", "r", stdin);
    freopen("/Users/fengyelei/Desktop/out", "w", stdout);
    int T, t, i, j, k;
    
    scanf("%d", &T);
    for (t=1;t<=T;t++) {
        scanf("%d", &n);
        for (i=0; i<n; i++) scanf("%lf", &a[i]);
        for (i=0; i<n; i++) scanf("%lf", &b[i]);
        sort(a, a+n);
        sort(b, b+n);
        printf("Case #%d: %d %d\n", t, f(), g());
    }
    return 0;
}
