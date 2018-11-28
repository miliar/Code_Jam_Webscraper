#include <cstdio>
#include <algorithm>
using namespace std;

int T, Case = 1, N;
double Nao[1001], Ken[1001];
int Deceitful();
int War();

int main()
{
    freopen("D-large.in", "rt", stdin);
    freopen("DoutLarge.txt", "wt", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) scanf("%lf", &Nao[i]);
        for (int i = 0; i < N; ++i) scanf("%lf", &Ken[i]);

        sort(Nao, Nao + N);
        sort(Ken, Ken + N);

        printf("Case #%d: %d %d\n", Case++, Deceitful(), War());
    }
}
int Deceitful()
{
    int num = 0;
    int i = 0, j = 0;  // i is the index for Naomi, j is for Ken
    for ( ; i < N; ++i)
        if (Nao[i] > Ken[j]) ++num, ++j;
    return num;
}
int War()
{
    int num = 0;
    int i = N - 1, j = N - 1;  // i is the index for Naomi, j is for Ken
    for ( ; i >= 0; --i) {
        if (Nao[i] > Ken[j])
            ++num;
        else
            --j;
    }
    return num;
}
