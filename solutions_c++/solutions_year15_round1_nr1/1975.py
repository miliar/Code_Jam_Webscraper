#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <stack>
#include <set>
#include <map>

using namespace std;

#ifdef DEBUG
    #define DBG(x) cerr<<#x<<"="<<(x)<<'\n'
#else
    #define DBG(x) static_cast<void>(0)
#endif

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i) ++)

pii solve(vector<int>& a) {
    int q1 = 0;
    int n = a.size();
    FOR(i, 1, n-1) {
        if (a[i] < a[i-1]) {
            q1 += a[i-1] - a[i];
        }
    }
    int q2 = 0;
    FOR (i, 1, n-1) {
        q2 = max(q2, a[i-1]-a[i]);
    }
    DBG(q2);
    int t = 0;
    FOR(i, 0, n-2) {
        t += min(q2, a[i]); 
    }
    return mp(q1, t);
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    in >> T;
    REP1(I,T) {
        cerr<<I<<"\n";
        int n;
        in >> n;
        vector<int> a(n);
        REP(i,n)
            in >> a[i];
        pii ans = solve(a);
        out<<"Case #"<<I<<": "<<ans.fi<<' '<<ans.se<<"\n";
    }

    in.close();
    out.close();
    return 0;
}

