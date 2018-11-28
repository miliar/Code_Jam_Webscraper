#include <iostream>
#include <algorithm>
using namespace std;

int arr[1005], T, N;

int possible(int val) {
    int eaten = 0;
    for (int a = 1; a < N; ++a) {
        if (arr[a - 1] - val > arr[a]) return -1;
        else eaten += min(val, arr[a - 1]);
    }
    return eaten;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    while (tc--) {
        int fir = 0;
        cin >> N;
        for (int a = 0; a < N; ++a)
            cin >> arr[a];
        for (int a = 1; a < N; ++a) {
            if (arr[a] < arr[a - 1])
                fir += arr[a - 1] - arr[a];
        }
        int lo = 0, hi = 10005, sec;
        while (lo <= hi) {
            int mid = (lo + hi) / 2,
                ans = possible(mid);
            if (ans != -1)
                hi = mid - 1, sec = ans;
            else
                lo = mid + 1;
        }
        cout << "Case #" << ++T << ": " << fir << " " << sec << "\n";
    }
    return 0;
}