
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
    bool f[17];
    scanf("%d", &T);
    for (t=1;t<=T;t++) {
        scanf("%d", &k);
        memset(f, 0, sizeof(f));
        for (i=0; i<16; i++) {
            scanf("%d", &j);
            if (i/4 == k-1) f[j] = 1;
        }
        scanf("%d", &k);
        int ans = -1;
        for (i=0; i<16; i++) {
            scanf("%d", &j);
            if (i/4 == k-1 && f[j]) {
                if (ans == -1) ans = j;
                else ans = -2;
            }
        }
        printf("Case #%d: ", t);
        if (ans > 0) printf("%d\n", ans);
        else if (ans == -1) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
