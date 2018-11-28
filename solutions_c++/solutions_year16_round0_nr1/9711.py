#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int tests;

void digi(vector<int> &ret, ll N) {
    ret.clear();
    while(N) {
        ret.push_back(N%10);
        N /= 10;
    }
}

int main() {
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        ll N;
        cin >> N;

        vector<int> tmp;
        digi(tmp, N);
        int cnt = tmp.size();
        int maxmult = pow(10, cnt+1);
        vector<bool>visi(10, false);
        int seen = 0;
        for (int i = 1; i <= maxmult; ++i) {
            digi(tmp, i*N);
            for (int j = 0; j < tmp.size(); ++j) {
                if (!visi[tmp[j]]) seen++;
                visi[tmp[j]] = true;
            }

            if (seen == 10) {
                cout << "Case #" << t << ": " << i * N << endl;
                break;
            }
        }

        if (seen < 10) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        }
    }

    return 0;
}