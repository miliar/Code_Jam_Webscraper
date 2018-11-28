#include <bits/stdc++.h>

using namespace std;

const int N  = 32;

bool divide (unsigned int mask,int  b, int x) {
    int p = 1;
    int res = 0;
    for (int i = 0; i < N; ++i) {
        res = (res + ((mask>>i)&1) * p)%x;
        p = (p * b) %x;
    }
    return res == 0;
}

int divisor (int mask, int b) {
    for (int x = 3; x <= 1000; x += 2) {
        if (divide (mask, b, x)) return x;
    }
    return -1;
}



int main (void) {
    int res = 0;
    int j = 0;
    cout << "Case #1:" << endl;
    for (unsigned int mask = 0; mask < (1<<30); ++mask) {
        vector <int> divisores;
        bool good = true;
        unsigned int m = (1<<N-1) + (mask<<1) + 1;
        for (int b = 2; b <= 10; ++b) {
            int r = divisor (m, b);
            if (r == -1) good = false;
            else divisores.push_back (r);
        }
        if (good) {
            ++j;
            for (int i = N-1; i >= 0; --i) {
                cout << ((m>>i)&1);
            }
            cout << " ";
            for (int i = 0; i < divisores.size(); ++i) cout << divisores[i] <<  " ";
            cout << endl;
        }
        if (j == 500) break;
    }
}
