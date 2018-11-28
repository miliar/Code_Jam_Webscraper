#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvin;

typedef long long LL;
typedef unsigned long long ULL;

struct Op {
    int s; char v;
    Op(int a, char b) {
        s = a;
        v = b;
    }
    bool is(const Op &other) {
        return (s==other.s&&v==other.v);
    }
};

Op multiple(Op a, Op b) {
    int s = a.s * b.s;
    if (a.v=='1') return Op(s, b.v);
    else if (b.v=='1') return Op(s, a.v);
    else if (a.v == b.v) return Op(-s, '1');
    else {
        if (a.v=='i' && b.v=='j') return Op(s, 'k');
        else if (a.v == 'i' && b.v == 'k') return Op(-s, 'j');
        else if (a.v == 'j' && b.v == 'i') return Op(-s, 'k');
        else if (a.v == 'j' && b.v == 'k') return Op(s, 'i');
        else if (a.v == 'k' && b.v == 'i') return Op(s, 'j');
        else if (a.v == 'k' && b.v == 'j') return Op(-s, 'i');
    }
    return Op(-1, '-');
}


int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int kk = 0;
    int T; cin >> T;

    while (T-- > 0) {
        kk++;
        cout << "Case #" << kk << ": ";
        int L; long long X; cin >> L >> X;
        string s; cin >> s;

        string total = "";
        for (long long i = 0; i < X; i++) total += s;
        if (total.size() < 3) {
            cout << "NO" << endl;
            continue;
        }
        int cp = 0;
        bool ii = false, jj = false, kk = false;
        Op pu = Op(1, '1'), iu = Op(1, 'i'), ju = Op(1, 'j'), ku = Op(1, 'k'), ou = Op(1, '1');
        Op cu(-1, '-');

        for (; cp < total.size(); cp++) {
            cu = multiple(pu, Op(1, total[cp]));
            pu = cu;
            if (cu.is(iu)) {
                ii = true;
                cp++;
                pu = ou;
                break;
            }
        }
        if (!ii) {
            cout << "NO" << endl;
            continue;
        }

        for (; cp < total.size(); cp++) {
            cu = multiple(pu, Op(1, total[cp]));
            pu = cu;
            if (cu.is(ju)) {
                jj = true;
                cp++;
                pu = ou;
                break;
            }
        }
        if (!jj) {
            cout << "NO" << endl;
            continue;
        }

        for (; cp < total.size(); cp++) {
            cu = multiple(pu, Op(1, total[cp]));
            pu = cu;
            if (cu.is(ku)) {
                kk = true;
                cp++;
                pu = ou;
                break;
            }
        }
        if (!kk) {
            cout << "NO" << endl;
            continue;
        }
        if (cp == total.size()) {
            cout << "YES" << endl;
            continue;
        }

        for (; cp < total.size(); cp++) {
            cu = multiple(pu, Op(1, total[cp]));
            pu = cu;
        }
        if (cu.is(ou)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}

