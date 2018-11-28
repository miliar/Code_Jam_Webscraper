#include <bits/stdc++.h>

using namespace std;
using LINT = long long int;
using PII = pair<int,int>;

#define PB push_back
#define FI first
#define SE second
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i, a, b) for(int i=(a);i<(b);++i)

int n, k;
double probs[17];

void process(int caseNum) {
    cin >> n >> k;
    REP(i, n) cin >> probs[i];

    double maxprob = 0;

    REP(x, (1<<n)) {
        bitset<16> test(x);

        if(test.count() != k) continue;

        vector<int> idxs;
        REP(y, n)
            if(test[y]) idxs.PB(y);

        // cout << idxs.size() << endl;


        double prob = 0;

        REP(y, (1<<k)) {
            bitset<16> test2(y);
            if(test2.count() != k/2) continue;

            double leprob = 1;
            REP(yy, k)
                if(test2[yy])
                    leprob *= probs[idxs[yy]];
                else
                    leprob *= 1-probs[idxs[yy]];

            prob += leprob;
        }

        maxprob = max(maxprob, prob);

    }

    cout << "Case #" << caseNum <<": ";
    cout << fixed << setprecision(6) <<  maxprob << endl;
}


int main() {
 int t;
    cin >> t;
    REP(i, t) process(i+1);

    return 0;
}
