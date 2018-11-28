#include <bits/stdc++.h>
using namespace std;

int T;

template <class TMP> void print(int i, TMP x) {
        cout << "Case #" << i << ": " << x << endl;
}

int main() {
    cin >> T;
    for(int tt = 1; tt <= T; ++tt) {
        string span;
        cin >> span;
        bool pan[100];
        int ns = span.size();
        int btm_bsup = 0;
        //char lastch = '\0';
        int npan = 0;
        for(int i = 0; i < ns; ++i) {
            char ch = span[i];
            if(ch == '+') {
                //lastch = ch;
                pan[i] = true;
                ++npan;
            }
            else if(ch == '-') {
                //lastch = ch;
                pan[i] = false;
                btm_bsup = i;
                ++npan;
            }
        }
        long long ans = 0;
        while(true) {
            int n_ssup = 0;
            for(int i = 0; i < npan; ++i) {
                if(pan[i]) ++n_ssup;
            }
            if(n_ssup == npan) break;
            while(btm_bsup >= 0) {
                if(!pan[btm_bsup]) {
                    pan[btm_bsup] = true;
                    --btm_bsup;
                }
                else {
                    for(int i = 0; i <= btm_bsup; ++i) {
                        pan[i] = !pan[i];
                    }
                    break;
                }
            }
            ++ans;
        }
        print(tt, ans);
    }
    return 0;
}
