#include <bits/stdc++.h>
using namespace std;
typedef long long int lint;
typedef long double ld;

int weight(int m) {
    int w = 0;
    while(m) {
        m = m & (m-1);
        w++;
    }
    return w;
}

void code() {
    int N, K;
    cin >> N >> K;
    vector<ld> P(N);
    for(int i = 0; i < N; i++) {
        cin >> P[i];
    }
    ld mv = 0;
    for(int m = 0; m < (1 << N); m++) {
        if(weight(m) != K) continue;
        ld p[16];
        int pp = 0;
        for(int i = 0; i < N; i++) {
            if(m & (1 << i)) {p[pp++] = P[i];}
        }
        ld p1[17];
        ld p2[17];
        p1[0] = 1;
        for(int i = 1; i <= K; i++) {
            p1[i] = 0;
        }

        for(int i = 0; i < K; i++) {
            p2[0] = p1[0] * (1-p[i]);
            for(int j = 1; j <= K; j++) {
                p2[j] = p[i] * p1[j-1] + (1-p[i]) * p1[j];
            }
            swap(p1, p2);
        }
        mv = max(mv, p1[K/2]);
    }
    cout << setprecision(9) << fixed << mv;
}

int main() {
    int t;
    cin >> t;
    for(int tt=1; tt<=t; tt++) {
        cout << "Case #" << tt << ": ";
        code();
        cout << endl;
    }
}
