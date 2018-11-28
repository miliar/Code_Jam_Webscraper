#include <cstdio>
#include <vector>
#include <map>
using namespace std;
int main() {
    int T, p;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d", &p);
        int e[p], f[p];
        for (int i=0; i<p; i++) scanf("%d", &e[i]);
        map<int, int> freq;
        for (int i=0; i<p; i++) {
            scanf("%d", &f[i]);
            freq[e[i]] = f[i];
        }
        vector<int> res, sums;
        sums.push_back(0);
        freq[0]--;
        for (int i=0; i<p; i++) {
            int x = e[i];
            if (freq[x] > 0) {
                res.push_back(x);
                int size = sums.size();
                for (int j=0; j<size; j++) {
                    freq[sums[j] + x]--;
                    sums.push_back(sums[j] + x);
                }
            }
            if (freq[x] > 0) i--;
        }
        printf("Case #%d: ", t);
        for (int x: res) printf("%d ", x);
        printf("\n");
    }
    return 0;
}
