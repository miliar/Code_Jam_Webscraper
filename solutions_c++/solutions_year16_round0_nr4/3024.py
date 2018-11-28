#include <iostream>

using namespace std;

long long int pow(long long int base, long long exp) {
    long long result = 1LL;
    while(exp>0) {
        if(exp%2 == 1)
            result = result*base;
        exp = exp >> 1;
        base = base*base;
    }
    return result;
}

int main() {
int T, K, C, S;
cin >> T;
for(int kase = 1; kase <= T; ++kase) {
    cin >> K >> C >> S;
    //long long int limit = pow(K,C);
    cout << "Case #" << kase << ":";
    /*
    for(int i = 0; i < K; ++i) {
        if((1+i*K) <= limit)
            cout << " " << 1+i*K;
        else break;
    }
    cout << "\n";
    */
    for(int i = 1; i <= K; ++i)
        cout << " " << i;
    cout << "\n";
}
    return 0;
}
