#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

int n, R, P, S;

string ans;

char winner(char x, char y) {
    if(x == y) return '?';
    if(x == 'R' && y == 'P') return 'P';
    if(x == 'P' && y == 'R') return 'P';
    if(x == 'R' && y == 'S') return 'R';
    if(x == 'S' && y == 'R') return 'R';
    if(x == 'S' && y == 'P') return 'S';
    if(x == 'P' && y == 'S') return 'S';
    return '?';
}

string go()
{
    int N = 1<<n; // 8
    ans = string(N, ' ');

    int r = R, p = P, s = S;
    auto valid = [&](string org) -> bool {
        string adv;
        string z = org;
        while(z.length() > 1) {
            adv.clear();
            for(int i = 0; i < (int)z.length(); i += 2) {
                char s = winner(z[i], z[i+1]);
                if(s == '?') return false;
                else adv += string(1, s);
            }
            z = adv;
   //         cout << "adv " << adv << endl;
        }
//        cout << org << " : " << "TRUE" << endl;
        return true;
    };
    function<string (int)> f = [&](int i) {
        if(i >= N) {
//            cout << "gen " << ans << endl;
            if( valid(ans) )
                return ans;
            else return string("");
        }
        else {
            string t;
            if(p) { ans[i] = 'P'; p--; t = f(i+1); p++; }
            if(t.size() > 0) return t;
            if(r) { ans[i] = 'R'; r--; t = f(i+1); r++; }
            if(t.size() > 0) return t;
            if(s) { ans[i] = 'S'; s--; t = f(i+1); s++; }
            if(t.size() > 0) return t;

            return t;
        }
    };

    string t = f(0);
    if(t.size() == 0) return "IMPOSSIBLE";
    return t;
}

int main() {
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; ++ kase)
    {
        cin >> n >> R >> P >> S;
        string ans = go();
        printf("Case #%d: %s\n", kase, ans.c_str());
    }

    return 0;
}

