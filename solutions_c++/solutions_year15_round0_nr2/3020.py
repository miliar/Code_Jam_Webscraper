#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i ++) {
        int D;
        cin >> D;
        vector<int> p(D);
        int max, min;
        for(int j = 0; j < D; j ++) {
            cin >> p[j];
            if(j == 0 || max < p[j]) {
                max = p[j];
            }
        }
        for(int d = max; d > 0; d --) {
            int res = d;
            for(int j = 0; j < D; j ++) {
                res += (p[j] - 1)/d;
            }
            if(max == d || min > res) {
                min = res;
            }

        }
        cout << "Case #" << i + 1 << ": " << min << endl;
    }

    return 0;
}
