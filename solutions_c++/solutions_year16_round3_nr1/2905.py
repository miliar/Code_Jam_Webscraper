#include <bits/stdc++.h>

using namespace std;
int cases = 1;
int n;
int arr[26];

int able(int lim) {
    for (int i = 0; i < n; ++i) {
        if (arr[i] > lim)return 0;
    }
    return 1;
}

int main(void) {
    freopen("/home/vanessi/ClionProjects/CodeJamR1CA/A.in","r",stdin);
    freopen("/home/vanessi/ClionProjects/CodeJamR1CA/A.out","w",stdout);
    int t;
    scanf("%d", &t);
    while (t--) {
        memset(arr, 0, sizeof arr);
        scanf("%d", &n);
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &arr[i]);
            sum += arr[i];
        }
        printf("Case #%d: ", cases++);
        if (sum % 2) {
            int maxi = 0, ind = -1;
            for (int i = 0; i < n; ++i) {
                if (arr[i] > maxi)maxi = arr[i], ind = i;
            }
            char an = 'A';
            arr[ind]--;
            an += ind;
            putchar(an);
            putchar(' ');
            sum--;
        }
        while (sum) {
            bool done = 0;
            for (int j = 0; j < n; ++j) {
                if (!arr[j])continue;
                for (int i = 0; i < n; ++i) {
                    if (!arr[j] || !arr[i])continue;
                    arr[j]--, arr[i]--;
                    if (able((sum - 2) / 2)) {
                        done = 1;
                        char an = 'A', bn = 'A';
                        an += i, bn += j;
                        putchar(an), putchar(bn);
                        sum -= 2;
                        if (sum)putchar(' ');
                        if (done)break;
                    } else arr[j]++, arr[i]++;
                }
                if (done)break;
            }
        }
        putchar('\n');
    }
}