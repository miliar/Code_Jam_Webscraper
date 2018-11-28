#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, ks = 0; cin >> T;
    int N;

    while(T--) {
        cout << "Case #" << ++ks << ": ";
        cin >> N;
        int NN = 0, ch_cnt = 0;
        bool ch[10] = {};
        if(N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        while(ch_cnt < 10) {
            NN += N;
            int t = NN;
            while(t > 0) {
                if(!ch[t % 10]) {
                    ch[t % 10] = true;
                    ++ch_cnt;
                }
                t /= 10;
            }
        }
        cout << NN << endl;
    }
    return 0;
}
