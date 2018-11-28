/**
*
*/
#include <bits/stdc++.h>
#define MAXN 100002
#define INF 200000000

typedef long long ll;
using namespace std;
string s;
int as[MAXN + 2], bs[MAXN + 2];

char winner(char left, char right) {
    if(left == 'R' && right == 'P') return 'P';
    else if(left == 'R' && right == 'S') return 'R';
    else if(left == 'R' && right == 'R') return '*';

    if(left == 'P' && right == 'P') return '*';
    else if(left == 'P' && right == 'S') return 'S';
    else if(left == 'P' && right == 'R') return 'P';

    if(left == 'S' && right == 'P') return 'S';
    else if(left == 'S' && right == 'S') return '*';
    else if(left == 'S' && right == 'R') return 'R';
}

int main() {
    freopen("A-small-attempt0 (3).in", "r", stdin);
    freopen("ancestor.out", "w", stdout);
    int n, r, p, s;
    int t; cin >> t; for(int i = 0; i < t; ++i) {
        string pattern;
        int found = 0;
        cin >> n >> r >> p >> s;
        for(int i = 0; i < r; ++i)pattern += "R";
        for(int i = 0; i < p; ++i)pattern += "P";
        for(int i = 0; i < s; ++i)pattern += "S";
        sort(pattern.begin(), pattern.end());
        do {
            string t = pattern;
            int inf_gl = 0;
            while(t.size() != 1) {
                int inf = 0;
                string new_t;
                for(int j = 0; j < t.size(); j += 2) {
                    char x = winner(t[j], t[j + 1]);
                    if(x == '*') {
                        inf = 1;
                        break;
                    }
                    else {
                        new_t += x;
                    }
                }
                if(inf) {
                    inf_gl = 1;
                    break;
                }
                t = new_t;
            }
            if(inf_gl == 0) {
                cout << "Case #" << i + 1 << ": " << pattern << endl;
                found = 1;
                break;
            }
        }
        while(next_permutation(pattern.begin(), pattern.end()));
        if(!found) cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
    }

}
