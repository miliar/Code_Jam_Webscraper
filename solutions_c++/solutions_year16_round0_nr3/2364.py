#include <bits/stdc++.h>
using namespace std;

int T;

template <class TMP> void print(int i, TMP x) {
        cout << "Case #" << i << ": " << x << endl;
}

unsigned long long divi(unsigned long long z)  {
    for(unsigned long long i = 2; i * i <= z; ++i) {
        if(z % i == 0) {
            return i;
        }
    }
    return 0;
}

int main() {
    cin >> T;
    int N, J;
    cin >> N >> J;

    cout << "Case #1:" << endl;

    if(T != 0 && (N != 16 || J != 50)) {
        cout << "DO NOT SUBMIT!" << endl;
        return 0;
    }

    unsigned long long zz = strtoull("1000000000000001", NULL, 2);
    unsigned long long z[9];
    int j = 0;
    //cout << zz << endl;
    while(j < J) {
        for(int i = 0; i < 9; ++i) {
            unsigned long long x = zz;
            unsigned long long zt = 0;
            unsigned long long base = 1;
            while(x) {
                if(x & 1ull) {
                    zt += base;
                }
                base = base * (i + 2);
                x = (x >> 1);
            }
            z[i] = zt;
        }
        zz += 2ull;
        //cout << zz << endl;
        unsigned long long dv[9];
        bool bflag = false;
        for(int i = 0; i < 9; ++i) {
            unsigned long long res = divi(z[i]);
            if(res == 0ull) {
                bflag = true;
                break;
            }
            dv[i] = res;
        }
        if(bflag) continue;

        unsigned long long x = z[0];
        stack<int> st;
        while(x) {
            st.push(x & 1ull);
            x = (x >> 1);
        }
        while(!st.empty()) {
            cout << st.top();
            st.pop();
        }
        cout << " ";
        for(int i = 0; i < 9; ++i) {
            cout << dv[i];
            if(i < 8) cout << " ";
            else cout << endl;
        }
        ++j;
    }

    return 0;
}
