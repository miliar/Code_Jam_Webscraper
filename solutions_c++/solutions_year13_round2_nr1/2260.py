#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int T;
int A;
int N;
int arr[10000010];
int tmp;
int ans = INT_MAX;
int caseCount = 1;

void dfs(int size, int index) {
    if (index >= N) {
        if (tmp < ans)
            ans = tmp;
        return;
    }
    if (size > arr[index]) {
        dfs(size + arr[index], index + 1);
    } else {
        tmp++;
        dfs(2 * size - 1, index);
        dfs(size, index + 1);
        tmp--;
    }
}

void solve() {
    sort(arr, arr + N);
    tmp = 0;
    ans = INT_MAX;
    if (A == 1) {
        ans = N;
    } else dfs(A, 0);
    cout << "Case #" << caseCount << ": " << ans << endl;
    caseCount++;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    cin >> T;
    while (T--) {
        cin >> A >> N;
        for (int i = 0; i < N; i++)
            cin >> arr[i];
        solve();
    }
    return 0;
}
