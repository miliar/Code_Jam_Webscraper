#include <iostream>
using namespace std;

long long int getBestRank(long long int N, long long int n) {
    n = (1LL<<N) - n;
    int wins = 0;
    while (n > 1) {
        n /= 2;
        wins++;
    }
    int lost = N - wins;
    long long int ans = 0;
    for (int i = 0; i < lost; i++) {
        ans *= 2;
        ans += 1;
    }
    return ans;
}

long long int getWorstRank(long long int N, long long int n) {
    int lost = 0;
    n++;
    while (n > 1) {
        lost++;
        n /= 2;
    }
    int i = 0;
    long long int ans = 0;
    for (; i < lost; i++) {
        ans *= 2;
        ans += 1;
    }
    for (; i < N; i++) {
        ans *= 2;
    }
    return ans;
}

int main() {

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        long long int N, P;
        cin >> N >> P;

        if (P == (1LL<<N)) {
            long long int ans = (1LL<<N) - 1;
            cout << "Case #" << t << ": " << ans << " " << ans << endl;
            continue;
        }

        long long int guaranteedWin = 0;
        long long int couldWin = 0;

        long long int lower = 0;
        long long int upper = (1LL<<N) - 1;
        while (lower <= upper) {
            long long int mid = (lower + upper) / 2;
            long long int bestMid = getBestRank(N, mid);
            long long int bestMid1 = getBestRank(N, mid+1);
            if (bestMid < P && bestMid1 >= P) {
                couldWin = mid;
                break;
            } else if (bestMid1 < P) {
                lower = mid;
            } else {
                upper = mid;
            }
        }

        lower = 0;
        upper = (1LL<<N) - 1;
        while (lower <= upper) {
            long long int mid = (lower + upper) / 2;
            long long int worstMid = getWorstRank(N, mid);
            long long int worstMid1 = getWorstRank(N, mid+1);
            if (worstMid < P && worstMid1 >= P) {
                guaranteedWin = mid;
                break;
            } else if (worstMid1 < P) {
                lower = mid;
            } else {
                upper = mid;
            }
        }

        cout << "Case #" << t << ": " << guaranteedWin << " " << couldWin << endl;
    }

    return 0;
}

