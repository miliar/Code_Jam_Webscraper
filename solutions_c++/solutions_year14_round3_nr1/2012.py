#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

long long gcd ( long long a, long long b )
{
    long long c;
    while ( a != 0 ) {
        c = a; a = b%a;  b = c;
    }
    return b;
}

struct frac {
    long long p;
    long long q;

    frac(long long a, long long b) {
        long long g = gcd(a, b);
        p = a / g;
        q = b / g;
    }
};

bool operator<(const frac &a, const frac &b) {
    /*
    long long g;
    g = gcd(a.q, b.q);
    long long aq = a.q / g;
    long long bq = b.q / g;
    return a.p * bq < aq * b.p;
    */
    return a.p * b.q < a.q * b.p;
}

int main()
{
    int T, t;
    int P, Q;
    char asdf;

    vector<map<frac, int> > combs;

    combs.push_back(map<frac, int>());
    combs[0][frac(0, 1)] = 40;
    combs[0][frac(1, 1)] = 0;

    for (int i = 1; i < 13; i++) {
        combs.push_back(map<frac, int>());
        for (auto j : combs[i - 1]) {
            combs[i][j.first] = j.second;
//            if (i < 4)
//                cout << j.first.p << "/" << j.first.q << ":" << j.second << " ";
        }
//            if (i < 4)
//                cout << endl;
        for (auto j : combs[i - 1]) {
            for (auto k : combs[i - 1]) {
                /*
                long long g = gcd(j.q, k.q);
                long long jq = j.q / g;
                long long kq = k.q / g;
                combs[i].insert(frac(j.p * kq + k.p * jq, jq * kq * g * 2));
                */
                frac nn = frac(j.first.p * k.first.q + k.first.p * j.first.q, j.first.q * k.first.q * 2);
                if (combs[i].find(nn) != combs[i].end())
                    combs[i][nn] = min(min(j.second, k.second) + 1, combs[i][nn]);
                else
                    combs[i][nn] = min(j.second, k.second) + 1;
            }
        }
//        cout << "asdf: " << i << ": " << combs[i].size() << endl;
    }

//    cout << "asdf" << endl;

    cin >> T;
    for (t = 1; t <= T; t++) {
        cin >> P >> asdf >> Q;
        int i;
        frac x(P, Q);
        int ans = 40;
        for (i = 0; i < 13; i++)
            if (combs[i].find(x) != combs[i].end()) {
                ans = min(ans, combs[i].find(x)->second);
            }
        if (ans < 40)
            cout << "Case #" << t << ": " << ans << "\n"; 
        else
            cout << "Case #" << t << ": " << "Impossible" << "\n"; 
    }
    return 0;
}
