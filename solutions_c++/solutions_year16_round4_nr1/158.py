#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;


const int R = 0, P = 1, S = 2;
const char id[] = "RPS";
int WIN[3][3] = {
    {0, 0, 1},
    {1, 0, 0},
    {0, 1, 0}
};


bool lss(const vector<int>& p1, const vector<int>& p2) {
    for (size_t i = 0; i < p1.size(); ++i) {
        char c1 = id[p1[i]]; 
        char c2 = id[p2[i]];
        if (c1 != c2)
            return c1 < c2;
    }
    return false;
}

vector<int> gen(int deep, int winner) {
    if (deep == 0) {
        return {winner};
    }
    for (int i = 0; i < 3; ++i) 
        if (i != winner && WIN[winner][i] == 1) {

            vector<int> p1 = gen(deep - 1, i);
            vector<int> p2 = gen(deep - 1, winner);

            if (lss(p1, p2)) {
                swap(p1, p2);
            }
            p2.insert(p2.end(), p1.begin(), p1.end());
            return p2;
        }
    assert(false);
}

unordered_map<int, unordered_map<int, unordered_map<int, vector<int> > > > ans;

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);

    for (int i = 1; i <= 12; ++i) {
        for (int k = 0; k < 3; ++k) {
            vector<int> vals = gen(i, k);
            vector<int> cnt(3);
            for (int x : vals) {
                ++cnt[x];
            }
            ans[ cnt[R] ][ cnt[P] ][ cnt[S] ] = vals;
        }
    }

    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {        
        int n, r, p, s;
        cin >> n >> r >> p >> s;

        cout << "Case #" << test << ": ";
        if (ans.count(r) && ans[r].count(p) && ans[r][p].count(s)) {
            const vector<int>& out = ans[r][p][s];
            for (int x : out) {
                cout << id[x];
            }            
        } else {
           cout << "IMPOSSIBLE";
        }

        cout << endl;
    }

    return 0;
}
