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

int solve(int n, string s) {
    int ans = 0;
    int k = 0;
    k += (s[0] - '0');
    DBG(n);
    DBG(s);
    FOR(i, 1, n) {
        DBG(ans);
        DBG(k);
        int c = s[i] - '0';
        if (c != 0) {
            if (i > k) {
                ans += i-k;
                k = c + i;
            }
            else {
                k+= c;
            }
        }
    }
    return ans;
}

int main() {
    ifstream in("input.a");
    ofstream out("output.a");
    int T;
    in >> T;
    REP1(I,T) {
        cerr<<I<<"\n";
        int n;
        string s;
        in>>n>>s;
        out<<"Case #"<<I<<": "<<solve(n, s)<<"\n";
    }
    in.close();
    out.close();
    return 0;
}
