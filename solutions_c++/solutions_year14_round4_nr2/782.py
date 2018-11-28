#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int N, T;
int a[1001], b[1001];

int main() {
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N;
        for(int i = 0; i < N; i++)
            cin >> a[i];
        int ans = 0;
        for(int i = 0; i < N; i++) {
            int cnt1 = 0;
            for(int j = 0; j < i; j++)
                if (a[i] < a[j])
                    cnt1++;
            int cnt2 = 0;
            for(int j = i + 1; j < N; j++)
                if (a[i] < a[j])
                    cnt2++;
            if (cnt1 < cnt2)
                ans += cnt1;
            else
                ans += cnt2;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
