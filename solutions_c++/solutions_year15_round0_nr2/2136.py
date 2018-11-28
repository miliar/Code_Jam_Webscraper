#include <iostream>
#include <queue>
using namespace std;
int T, N;
int a[1005];
const int INF = 1e9;
int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N;
        priority_queue<int> p;
        for(int i = 1; i <= N; i++) {
            cin >> a[i];
        }
        int best = INF;
        for(int i = 1; i <= 1000; i++) {
            int cur = 0;
            for(int j = 1; j <= N; j++) {
                int req = (a[j]/i) + (a[j]%i ? 1 : 0);
                req--;
                cur += req;
            }
            best = min(best, cur+i);
        }
        cout << "Case #" << t << ": " << best << "\n";
    }

    return 0;
}
