#include <bits/stdc++.h>
using namespace std;

bool check(int f, const string& levels) {
    int n = levels.length();
    for (int i = 0; i < n; i++) {
        int l = levels[i] - '0';
        if (l > 0 && f < i) {
            return false;
        }
        f += l;
    }
    return true;
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int Smax;
        string levels;
        cin >> Smax >> levels;
        int low = 0, high = 1001;
        while (low < high) {
            int mid = (low + high) / 2;
            if (check(mid, levels)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        cout << "Case #" << tc << ": " << low << endl;
    }
        
    return EXIT_SUCCESS;
}
