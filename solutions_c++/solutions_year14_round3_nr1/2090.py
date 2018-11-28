#include <iostream>
#include <queue>

using namespace std;

typedef unsigned long long int ULLI;

void reduce(ULLI &p, ULLI &q) {
    ULLI sq = min(p, q)*min(p, q);
    for (int n=2; (ULLI)n<=sq; n++) {
        if (p%n == 0 && q%n == 0) {
            p /= n;
            q /= n;
            n--;
            sq = min(p, q)*min(p, q);
        }
    }
}

int solve(ULLI p, ULLI q) {
    int b = 2;
    int n_min = 40;
    if (p == q) {
        return 0;
    }
    for (int n=1; n<=40; n++) {
        reduce(p, q);
        ULLI pb = p*b;
        if (pb >= q) {
            n_min = min(n, n_min);
            if (pb == q) {
                return n_min;
            }
            p = pb-q;
            q *= b;
        }
        b += b;
    }
    return -1;
}

int main() {
    int t, answer;
    ULLI p, q;
    cin >> t;
    for (int case_num=1; case_num<=t; case_num++) {
        cin >> p;
        cin.ignore(1);
        cin >> q;
        answer = solve(p, q);
        cout << "Case #" << case_num << ": ";
        if (answer < 0) {
            cout << "impossible" << endl;
        }
        else {
            cout << answer << endl;
        }
    }
    return 0;
}
