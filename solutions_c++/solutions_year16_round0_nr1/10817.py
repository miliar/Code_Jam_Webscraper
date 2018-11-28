
#include <bits/stdc++.h>

using namespace std;

inline bool getBit(int n, int idx) { return n & (1 << idx); }
inline int setBit(int n, int idx) { return n | (1 << idx); }

int T, N, seen, cnt = 0;

void proc(int n){
    while(n > 0){
        seen = setBit(seen, n % 10);
        n = n / 10;
    }
}

int solve(){
    seen = 0;
    int d = N;
    while(true){
        int l = seen;
        proc(N);

        if (l == seen){
            cnt++;
        } else {
            cnt = 0;
        }

        if (cnt > 100) return -1;

        if (seen == 1023){
            return N;
        }

        //if (N > 100000 || N == 0) return -1;
        N += d;
    }
}

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> T;
    for (int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        cin >> N;

        int r = solve();
        if (r == -1){
            cout << "INSOMNIA\n";
        } else {
            cout << r << "\n";
        }
    }
}
