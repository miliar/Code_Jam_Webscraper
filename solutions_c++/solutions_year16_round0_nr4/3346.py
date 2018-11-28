#include <iostream>

using namespace std;

long long ipow(long long base, long long exp) {
    // from http://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-an-integer-based-power-function-powint-int
    long long result = 1;
    while (exp) {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

void compute(int K, int C, int S) {
    S=S; // supress the warning, we are here in the simple case where S=K
    long long step = ipow(K, C-1);
    for(long long i = 0 ; i < K ; i++) {
        cout << " " << i*step+1;
    }
}

int main() {
    int T;
    int K, C, S;
    cin >> T;
    for(int i = 1 ; i <= T ; i++) {
        cin >> K >> C >> S;
        cout << "Case #" << i << ":";
        compute(K, C, S);
        cout << "\n";
    }
    return 0;
}
