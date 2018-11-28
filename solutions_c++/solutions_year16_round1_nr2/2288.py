#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <map>
#include <cstring>
using namespace std;

#define N 101

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, n, m;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d", &n);
        std::map<int, int> counter;
        for (int j = 0; j < 2 * n - 1; ++j) {
            for (int k = 0 ; k < n; k++) {
                scanf("%d", &m);
                counter[m]++;
            }
        }
        std::vector<int> ret;
        for (std::map<int, int>::iterator it = counter.begin(); it != counter.end(); it++) {
            if (it->second % 2 == 1)
                ret.push_back(it->first);
        }
        printf("Case #%d:", i);
        std::sort(ret.begin(), ret.end());
        for (int j = 0; j < ret.size(); ++j) {
            printf(" %d", ret[j]);
        }
        puts("");
    }
    return 0;
}
