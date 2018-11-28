#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) ((int)(c).size())
#define sqr(x) ((x)*(x))
#define REP(i, c) for(int i=0; i<c; i++)
#ifdef ONLINE_JUDGE
    #define WAIT
#else
    #define WAIT cout<<flush, system("PAUSE")
#endif

typedef long long ll;
typedef pair<int, int> pii;

int solve(string & s) {
    s += '+';
    int sol = 0;
    for (int i = 1; i < SZ(s); i++)
        if (s[i] != s[i-1])
            sol++;
    return sol;
}

int tc;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> tc;
    for (int ti = 1; ti <= tc; ti++) {
        cin >> s;
        cout << "Case #" << ti << ": " << solve(s) << endl;
    }

//    WAIT;
}
