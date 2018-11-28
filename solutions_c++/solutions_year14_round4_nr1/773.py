#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int N, T, X;
int a[10001];

int main() {
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for(int t = 1; t <= T; t++) {
        cin >> N >> X;
        for(int i = 0; i < N; i++)
            cin >> a[i];
        sort(a, a + N);
        int ans = 0, j = N - 1;
        for(int i = 0; i <= j; i++) {
            while (j > i && a[i] + a[j] > X) {
                j--;
                ans++;
            }
            if (j > i && a[i] + a[j] <= X) {
                ans++;
                j--;
            } else {
                ans++;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
	}
    return 0;
}
