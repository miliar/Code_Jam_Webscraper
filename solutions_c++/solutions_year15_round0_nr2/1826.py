#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
const int N = 1100;
vector<int> a;

int main() {
    int o, n, cas = 0;
    scanf("%d", &o);
    while (o--) {
        scanf("%d", &n);
        //n = 1000;
        a.clear();
        int x, m = -1;
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            //x = 1000;
            a.push_back(x);
            m = max(m, x);
        }
        int res = m;
        for (int i = 1; i <= m; i++) {
            int sum = i;
            for (int k = 0; k < n; k++)
                if (a[k] > i) {
                    if (a[k] % i == 0)
                        sum += a[k] / i - 1;
                    else
                        sum += a[k] / i;
                }
            //cout<<i<<' '<<sum<<endl;
            res = min(res, sum);
        }
        printf("Case #%d: %d\n", ++cas, res);
    }
    return 0;
}