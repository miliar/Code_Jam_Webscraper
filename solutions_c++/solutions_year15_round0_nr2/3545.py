#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>

using namespace std;

int a[100005];

int main() {
    int t;

   // cin >> t;
    int tst = 0;
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
 //  cout << "hello" << endl;
    cin >> t;
    while(t--) {
        tst++;
        int n;
        cin >> n;
        priority_queue<int> pq;
        for(int i = 0; i < n; i++) cin >> a[i];
        sort(a, a+n);
        reverse(a, a+n);
        int ans = 1000000000;

        for(int i = 1; i <= a[0]; i++) {
            int tot = 0;
            int maxval = 0;
            for(int j = 0; j < n; j++) {
                maxval = max(maxval, (a[j]<=i)?a[j]:i);
                tot += ((a[j]+i-1)/i - 1);
            }
            ans = min(ans, tot+maxval);
        }
        cout << "Case #" << tst << ": " << ans << endl;
    }
}
