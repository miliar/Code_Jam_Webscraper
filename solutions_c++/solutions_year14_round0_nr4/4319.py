#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
double A[1005];
double B[1005];
int n;

int solve1() {
    int mina = 0, maxa = n - 1;
    int minb = 0, maxb = n - 1;
    int ans = 0;
    while (mina <= maxa) {
        if (A[maxa] > B[maxb]) {
            ans++;
            maxa--;
            maxb--;
        } else if (A[mina] > B[minb]) {
            ans++;
            mina++;
            minb++;
        } else {
            mina++;
            maxb--;
        }
    }
    return ans;
}

int solve2() {
    int posa = 0;
    int posb = 0;
    int ans = 0;
    while (posa < n && posb < n) {
        int i;
        for (i = posb; i < n; i++) {
            if (B[i] > A[posa]) {
                posb = i + 1;
                posa++;
                ans++;
                break;
            }
        }
        if (i == n)break;
    }
    return n - ans;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w",stdout);
    int i;
    int T;
    int cas = 1;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        for (i = 0; i < n; i++)
            scanf("%lf",A + i);
        for (i = 0; i < n; i++)
            scanf("%lf",B + i);
        sort(A, A + n);
        sort(B, B + n);
        int ans1 = solve1();
        int ans2 = solve2();
        printf("Case #%d: %d %d\n",cas++, ans1, ans2);
    }
    return 0;
}
