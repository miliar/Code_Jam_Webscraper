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

int solve(int n) {
    set<int> digits;
    int k = 0;
    while (digits.size() < 10) {
        k ++;       
        int q = k*n;
        while (q) {
            digits.insert(q % 10);
            q /= 10;
        }
    }
    return k*n;
}

const int MAXN = 1000000;
vector<int> ans(MAXN+1);

int main() {
    for (int i = 1; i <= MAXN; i++) {
        ans[i] = solve(i);
    }
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    in >> T;
    REP1(I,T) {
        cerr<<I<<"\n";
        int n;
        in >> n;
        out<<"Case #"<<I<<": ";
        if (n == 0)
            out<< "INSOMNIA";
        else out<<ans[n];
        out<<"\n";
    }

    in.close();
    out.close();
    return 0;
}
