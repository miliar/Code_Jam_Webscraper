#include<iostream>
using namespace std;

int T;
long long K, C, S;

long long doPow(long long x, int y) {
    if (y == 0)
        return 1;
    if (y == 1)
        return x;
    else {
        long long cur = doPow(x, y / 2);
        if (y % 2 == 0)
            return cur * cur;
        else
            return cur * cur * x;
    }
}

long long get_index(int start, int count) {
    long long ans = 0;
    int l = 1;
    for (int i = 0; i < count; i++) {
        ans += (start + i) * doPow(K, C - l);
        l++;
    }
    return ans;
}

int main() {
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> K >> C >> S;
        cout << "Case #" << t + 1 << ": ";
        if (S*C < K) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        int start = 0;
        while (start < K) {
            if (start + C < K) {
                cout << get_index(start, C) + 1 << " ";
                start += C;
            }
            else {
                cout << get_index(start, K - start) + 1 << " ";
                start = K;
            }
        }
        cout << endl;
    }
    return 0;
}
