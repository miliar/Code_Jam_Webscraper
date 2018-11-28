#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>

using namespace std;
inline unsigned CheckAudience(unsigned* S, unsigned Smax) {
    unsigned sum = S[0]; // 0 shyness level
    unsigned output = 0;

    for (unsigned i = 1; i <= Smax; i++) {
        if (sum < i ) {
            output += (i - sum);
            sum = i;
        } 
        sum += S[i];
    }

    return output;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    unsigned T,Smax;
    unsigned S[1000];

    cin >> T;
    for (unsigned i = 0; i < T; i++) {
        string num;
        cin >> Smax;
        cin >> num;
        for (unsigned j = 0; j <= Smax; j++) {
            char c = num[j];
            S[j] = c - '0';
        }
        cout << "Case #" << (i+1) << ": ";
        cout << CheckAudience(&S[0], Smax) << endl;
    }

    return 0;
}
