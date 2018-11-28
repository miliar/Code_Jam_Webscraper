#include <iostream>
#include <algorithm>
using namespace std;

long long getAns1(int N, long long P) {
    if (P == (1LL<<N))
        return P-1;
    if ( (1LL<<N) >= 2*P )
        return 0;
    return 2*(1 + getAns1(N - 1, P - (1LL<<(N-1))));
}

long long getAns2(int N, long long P) {
    if (P == (1LL<<N))
        return P-1;
    if (P >= (1LL<<(N-1)))
        return (1LL<<N)-2;
    return 2*getAns2(N-1, P);
}

int main(void) {
    int T;
    cin >> T;
    for (int testNo = 1; testNo <= T; ++testNo) {
        int N;
        long long P;
        cin >> N >> P;
        cout << "Case #" << testNo << ": " << getAns1(N, P) << " " << getAns2(N, P) << endl;
    }
    return 0;
}