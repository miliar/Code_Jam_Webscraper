#include <iostream>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;



int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, i, c, D, n, maximum, res, total, j, k;
    
    scanf("%d", &T);
    
    for (c = 1; c <= T; c++) {
        printf("Case #%d: ", c);
        scanf("%d", &D);
        vector<int>v;
        maximum = -1;
        for (k = 0; k < D; k++) {
            scanf("%d", &n);
            maximum = max(maximum, n);
            v.push_back(n);
        }
        res = 1000000;
        for (i = 1; i <= maximum; i++) {
            total = 0;
            for (j = 0; j < v.size(); j++) {
                if (v[j] > i) {
                    total += v[j] / i;
                    if (v[j] % i == 0) total--;
                }
            }
            total += i;
            res = min(res, total);
        }
        printf("%d\n", res);
    }
    
    return 0;
}
