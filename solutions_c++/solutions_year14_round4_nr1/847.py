#include <cstdio>
#include <algorithm>
#include <cstdio>
using namespace std;
int arr[10000];
bool used[10000];
int main() {
    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        int n, x;
        scanf("%d %d", &n, &x);
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
            used[i] = false;
        }
        sort(arr, arr + n);
        reverse(arr, arr + n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!used[i]) {
                used[i] = true;
                for (int j = i + 1; j < n; j++) {
                    if (!used[j] && arr[i] + arr[j] <= x) {
                        used[j] = true;
                        break;
                    }
                }
                ans++;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}


