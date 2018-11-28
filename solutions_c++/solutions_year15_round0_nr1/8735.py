#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<utility>

using namespace std;

#define T_MAX 100
#define S_MAX 1001

int aggShy[S_MAX];
int shy[S_MAX];
int n;

int solve() {
    return 0;
}

int main() {
    FILE* in = fopen("small.in", "r");
    FILE* out = fopen("small.out", "w");

    int t = 0;
    fscanf(in, "%d", &t);

    char tmp;
    for (int i = 0; i < t; ++i) {
        fscanf(in, "%d", &n);
        fscanf(in, "%c", &tmp);
        aggShy[0] = 0;
        for (int j = 0; j <= n; ++j) {
            fscanf(in, "%c", &tmp);
            int val = tmp - '0';
            if (j == 0) {
                aggShy[j] = val;
            }
            else {
                aggShy[j] = aggShy[j - 1] + val;
            }
        }

        int ret = 0;
        for (int j = 0; j <= n; ++j) {
            if (j != 0 && j - aggShy[j-1] > ret) {
                ret = j - aggShy[j-1];
            }
        }
        fprintf(out, "Case #%d: %d\n", i + 1, ret);
    }
    fclose(in);
    fclose(out);

    return 0;
}
