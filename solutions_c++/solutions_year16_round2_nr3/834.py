#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; t++) {
        int n;
        cin >> n;
        vector<string> fi(n), se(n);
        for (int i=0; i<n; i++) {
            cin>>fi[i]>>se[i];
        }
        int result = 0;

        for (int mask=0; mask<(1<<n); mask++) {
            set<string> sfi, sse;

            for (int i=0; i<n; i++) {
                if (mask & (1<<i)) {
                    sfi.insert(fi[i]);
                    sse.insert(se[i]);
                }

            }
            int suc = 1, amo = 0;
            for (int i=0; i<n; i++) {
                if ( ! (mask & (1 << i))) {
                    if (sfi.find(fi[i]) == sfi.end() || sse.find(se[i]) == sse.end()) {
                        suc = 0;
                        break;
                    }
                    amo++;
                }
            }
            if (suc) {
                result = max(result, amo);
            }
        }
        printf("Case #%d: %d\n", t, result);
    }
    return 0;
}
