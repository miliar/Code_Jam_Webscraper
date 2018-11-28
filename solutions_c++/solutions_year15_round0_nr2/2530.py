#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

const int N = 1010;

int m;
int cake[N];

int turn(void)
{
    int cktmp[N];
    memcpy(cktmp, cake, N * sizeof(int));
    int mtmp = m, ttmp = 0;
    while (1) {
        int half = mtmp >> 1;
        cktmp[half] += cktmp[mtmp];
        cktmp[mtmp - half] += cktmp[mtmp];
        ttmp += cktmp[mtmp];
        cktmp[mtmp] = 0;
        int i;
        for (i = mtmp - 1; i > 0; i--) {
            if (cktmp[i] > 0)
                break;
        }
        mtmp = i;
        if (mtmp == 0)
            break;
        if (mtmp + ttmp <= m) {
            m = mtmp;
            memcpy(cake, cktmp, N * sizeof(int));
            return ttmp;
        }
    }
    return -1;
}

int turn_with9(void)
{
    int cktmp[N];
    memcpy(cktmp, cake, N * sizeof(int));
    int mtmp = m, ttmp = 0;
    while (1) {
        int half = mtmp == 9 ? 3 : mtmp >> 1;
        cktmp[half] += cktmp[mtmp];
        cktmp[mtmp - half] += cktmp[mtmp];
        ttmp += cktmp[mtmp];
        cktmp[mtmp] = 0;
        int i;
        for (i = mtmp - 1; i > 0; i--) {
            if (cktmp[i] > 0)
                break;
        }
        mtmp = i;
        if (mtmp == 0)
            break;
        if (mtmp + ttmp <= m) {
            m = mtmp;
            memcpy(cake, cktmp, N * sizeof(int));
            return ttmp;
        }
    }
    return -1;
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int d, p;
        scanf("%d", &d);
        memset(cake, 0, sizeof(cake));
        m = 0;
        while (d--) {
            scanf("%d", &p);
            m = max(m, p);
            cake[p]++;
        }
        int mbak = m;
        int ckbak[N];
        memcpy(ckbak, cake, N * sizeof(int));
        int res = 0, tmp;
        while (m > 3 && (tmp = turn()) != -1)
            res += tmp;
        res += m;
        m = mbak;
        memcpy(cake, ckbak, N * sizeof(int));
        int res9 = 0, tmp9;
        while (m > 3 && (tmp9 = turn_with9()) != -1)
            res9 += tmp9;
        printf("Case #%d: %d\n", cases, min(res, res9 + m));
    }
    return EXIT_SUCCESS;
}
