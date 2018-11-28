#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int n;
int space;
int disks[10000];

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d %d", &n, &space);
        int i;
        for (i = 0; i < n; i++)
            scanf("%d", &disks[i]);
        sort(disks, disks+n);
        int j = n-1;
        int pairs = 0;
        for (i = 0; i < j; i++) {
            for (; disks[i] + disks[j] > space && j > i; j--);
            if (i != j && disks[i]+disks[j] <= space) {
                 j--;
                 pairs++;
            }
        }
        printf("%d\n", n - pairs);
    }
}