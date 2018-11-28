#include <iostream>

using namespace std;

#define MAXN 1001

int
war(const double *ken, const double *naomi, int N)
{
    int i, j;

    i = j = 0;

    while (i < N) {
        while (j++ < N) {
            if (naomi[j - 1] > ken[i]) {
                ++i;
                break;
            }
        }
        if (j > N) {
            break;
        }
    }
    return N - i;
}

int
deceitful(const double *ken, const double *naomi, int N)
{
    if (N == 0) return 0;

    if (ken[0] > naomi[0]) {
        if (ken[N - 1] > naomi[N - 1]) return deceitful(ken + 1, naomi + 1, N - 1) + 1;
        else return deceitful(ken + 1, naomi, N - 1);
    } else {
        return deceitful(ken + 1, naomi, N - 1);
    }
}

int main(int argc, char *argv[])
{
    int T, N;
    double ken[MAXN], naomi[MAXN];

    scanf("%d", &T);
    for (int k = 1; k <= T; ++k) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) scanf("%lf", &ken[i]);
        for (int i = 0; i < N; ++i) scanf("%lf", &naomi[i]);

        sort(ken, ken + N);
        sort(naomi, naomi + N);

        printf("Case #%d: %d %d\n", k, deceitful(ken, naomi, N), war(ken, naomi, N));
    }
    return 0;
}
