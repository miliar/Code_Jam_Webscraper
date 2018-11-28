#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 10005

int file[N], n, disc;
bool marked[N];

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int cas;
    scanf("%d", &cas);
    for (int _cas = 1; _cas <= cas; _cas++) {
        scanf("%d%d", &n, &disc);
        memset(marked, false, sizeof(marked));
        for (int i = 0; i < n; i++)
            scanf("%d", &file[i]);
        sort(file, file + n);

        int result = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (marked[i])
                continue;
            marked[i] = true;
            for (int j = i - 1; j >= 0; j--) {
                if (marked[j])
                    continue;
                if(file[i] + file[j] <= disc){
                    marked[j] = true;
                    break;
                }
            }
            result++;
        }
        printf("Case #%d: %d\n", _cas, result);
    }
    return 0;
}
