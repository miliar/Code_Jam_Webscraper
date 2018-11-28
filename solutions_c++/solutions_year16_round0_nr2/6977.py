#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <stack>
#include <set>
#include <map>
#include <string>

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

int solve(string s) {
    char c = s[0];
    int ans = 0;
    for (int i = 1; i < (int)s.size(); i++) {
        if (s[i] != c) {
            ans ++;
            if (c == '+')
                c = '-';
            else 
                c = '+';
        }
    }
    if (c == '-')
        ans ++;
    return ans;
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    in >> T;
    REP1(I,T) {
        cerr<<I<<"\n";
        string s;
        in >> s;
        out<<"Case #"<<I<<": "<<solve(s)<<"\n";
    }

    in.close();
    out.close();
    return 0;
}
