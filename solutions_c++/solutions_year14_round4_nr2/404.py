#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int n;
int seq[1000];

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d", &n);
        int i, j;
        for (i = 0; i < n; i++)
            scanf("%d", &seq[i]);
        
        int ans = 0;
        int start = 0;
        int end = n-1;
        for (i = 0; i < n; i++) {
            int min = start;
            for (j = start; j <= end; j++)
                if (seq[j] < seq[min])
                    min = j;
            if (min - start < end - min) {
                ans += min - start;
                int curr = seq[min];
                for (j = min; j > start; j--)
                    seq[j] = seq[j-1];
                seq[start] = curr;
                start++;
                continue;
            }
            ans += end - min;
            int curr = seq[min];
            for (j = min;j < end; j++)
                seq[j] = seq[j+1];
            seq[end] = curr;
            end--;
        }
        printf("%d\n", ans);
    }
}