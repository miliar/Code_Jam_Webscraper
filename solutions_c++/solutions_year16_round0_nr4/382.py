#include <iostream>

using namespace std;

typedef unsigned long long ll;

ll pow(ll base, ll exp)
{
    ll result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

void solve(ll K, ll C, ll S) {
    if(S * C < K) {
        cout << " IMPOSSIBLE" << endl;
        return;
    }

    ll k = 0;
    for(int c = 0; c < K; c += C) {
        ll check = 0;
        for(int i = 0; i < C; ++i) {
            check += k * pow(K, C - i - 1);
            k = min(K-1, k+1);
        }
        cout << " " << check + 1;
        if(check + 1 > pow(K, C)) {
            cout << " BOOM!" << endl;
        }
    }
    cout << endl;
}

int main() {

    int T;
    cin >> T;
    int c = 1;
    while(T --> 0) {
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << c++ << ":";
        solve(K, C, S);
    }

    return 0;
}