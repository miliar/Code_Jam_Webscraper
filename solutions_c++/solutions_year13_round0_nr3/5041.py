#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool ispal(long long x) {
    long long y = 0;
    if (x == 0)
        return true;
    long long cx = x;
    while (x > 0) {
        y = y * 10 + x % 10;
        x /= 10;
    }
    return cx == y;
}

vector<long long> a;

void precalc() {
    for (int i = 1; i <= 10000000; ++i) {
        if (ispal(i) && ispal(i * i)) {
            a.push_back(i * i);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    precalc();
   
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long A, B;
        cin >> A >> B;
        int res = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] >= A && a[i] <= B)
                ++res;
        }
        cout << "Case #" << t << ": " << res << endl;
       
    }
    
    return 0;
}