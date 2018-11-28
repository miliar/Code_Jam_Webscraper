#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

#define print(x) cout << x << endl
#define input(x) cin >> x

const int SIZE = 32100;

int n, t;
int A[SIZE];
char flag[SIZE];

int main()
{
    freopen("input.txt", "r", stdin);
    int T = 1, cas = 1;
    input(T);
    while (T--) {
        // input(t >> n);
        input(n >> t);
        for (int i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        memset(flag, 0, sizeof(flag));
        int p, q;
        p = 0;
        q = n - 1;
        int ans = 0;
        sort(A, A + n);
        while (p < q) {
            while (p < q && A[p] + A[q] > t) {
                ans++;
                q--;
            }
            if (p < q) {
                p++;
                q--;
                ans++;
            }
        }
        if (p == q) ans++;
        printf("Case #%d: ", cas++);
        print (ans);
    }
    return 0;
}

