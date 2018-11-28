#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int n;
        scanf("%d", &n);
        double naomi[n], ken[n];
        for (int j = 0; j < n; j++) scanf("%lf", &(naomi[j]));
        for (int j = 0; j < n; j++) scanf("%lf", &(ken[j]));
        sort(naomi, naomi + n);
        sort(ken, ken + n);
        int dw = 0;
        int j, t = 0;
        for (j = 0; j < n && naomi[j] < ken[n - t - 1]; j++) {
            if (naomi[j] > ken[dw]) dw++;
            else t++;
        }
        dw += n - j;
        int w = 0;
        t = 0;
        for (j = n - 1; j >= 0; j--) {
            while (ken[n - t - 1] == -1) t++;
            if (naomi[j] > ken[n - t - 1]) w++;
            else {
                int k;
                for (k = 0; ken[k] < naomi[j]; k++);
                ken[k] = -1;
                if (k == n - t - 1) t++;
            }
        }
        printf("Case #%d: %d %d\n", i+1, dw, w);
    }
    return 0;
}
