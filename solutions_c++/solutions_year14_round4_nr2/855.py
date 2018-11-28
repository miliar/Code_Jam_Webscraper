#include <cstdio>
#include <algorithm>
#include <cassert>
#define F first
#define S second
#define INF 1000000000
using namespace std;
pair<int, int> arr[1002];
bool taken[1002];
int main() {
    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            int val;
            scanf("%d", &val);
            arr[i].F = val;
            arr[i].S = i;
        }
        sort(arr, arr + n);
        for (int i = 0; i < n; i++) {
            taken[i] = false;
        }
        int ans = 0;
        for (int k = 0; k < n; k++) {
            int pos = arr[k].S;
            int left = 0;
            int right = 0;
            for (int i = 0; i < pos; i++) {
                if (!taken[i]) left++;
            }
            for (int i = pos + 1; i < n; i++) {
                if (!taken[i]) right++;
            }
            taken[pos] = true;
            ans += min(left, right);
        }
        printf("Case #%d: %d\n", test, ans);


    }
    return 0;
}


