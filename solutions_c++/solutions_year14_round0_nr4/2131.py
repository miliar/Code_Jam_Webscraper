#include <cstdio>
#include <utility>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
#define FOR(x, b, e) for(int (x)=(b); x<=(e); ++(x))
#define FORD(x, b, e) for(int (x)=(b); x>=(e); ––(x))
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PII pair<int, int>

int get_deceived(list<LD> a, list<LD> b) {
    a.sort();
    b.sort();
    int res = 0;
    auto ita = a.begin();
    auto itb = b.begin();
    while (ita != a.end()) {
        while (*ita < *itb)
            ita++;
        if (ita != a.end()) {
            ita++; itb++;
            res++;
        }
    }
    return res;
}

int get_honest(list<LD> a, list<LD> b, int n) {
    a.sort();
    b.sort();
    int res = 0;
    auto itb = b.begin();
    FOREACH(ita, a) {
        while (itb != b.end() && *itb < *ita)
            itb++;
        if (itb != b.end()) {
            res++;
            itb++;
        }
    }
    return n - res;
}

int main() {
    int t;
    cin >> t;
    FOR(z, 1, t) {
        int N;
        cin >> N;
        list<LD> s[2];
        REP(i, 2) {
            REP(j, N) {
                LD temp;
                cin >> temp;
                s[i].PB(temp);
            }
        }
        cout << "Case #" << z << ": " << get_deceived(s[0], s[1]) << " " << get_honest(s[0], s[1], N) << endl;
    }
    return 0;
}
