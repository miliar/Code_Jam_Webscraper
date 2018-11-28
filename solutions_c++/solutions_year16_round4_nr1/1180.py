#define _USE_MATH_DEFINES

#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <queue>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <climits>
#include <cstring>

using namespace std;

typedef long long ll;

int const INF = 1000 * 1000 * 1000 + 11;
ll const LINF = (ll)INF * INF;

const vector<string> type = {"R", "P", "S"};

struct Pos {
    int first;
    int second;
    
    string res;
    
    Pos(int first, int second, string res) : first(first), second(second), res(res) {}
    
    bool operator<(Pos const &p) const {
        if (first == p.first) return second < p.second;
        return first < p.first;
    }
};

string solve(int const n, int r, int p, int s) {
    vector<int> cnt = {r, p, s};
    
    vector<vector<int> > graph(n);
    vector<set<Pos>> verts(3);
    
    
    int m = max(r, max(p, s));
    
    vector<vector<int>> ccnt(3, vector<int>(n + 5, 0));
    
    //if (m > r + p + s - m) return "IMPOSSIBLE";
    
    
    int done = 0;
    for (int i = 0; i != 3; ++i) {
        ccnt[i][1] = cnt[i];
        
        for (int j = 0; j != cnt[i]; ++j) {
            verts[i].insert(Pos(1, ++done, type[i]));
        }
    }
    
    int last = 0;
    for (int i = 0; i != (1 << n) - 1; ++i) {
        int choose = -1;
        
        for (int j = 0; j != 3; ++j) {
            if (cnt[j] && cnt[(j + 1) % 3] &&
                verts[j].begin()->first == verts[(j + 1) % 3].begin()->first) {
                
                if (choose == -1) {
                    choose = j;
                } else {
                    int level = verts[j].begin()->first;
                    int choose_level = verts[choose].begin()->first;
                    
                    if (level < choose_level || (level == choose_level && ccnt[j][level] > ccnt[choose][level])) {
                        choose = j;
                    }
                }
            }
        }
        
        if (choose == -1) {
            return "IMPOSSIBLE";
        }
        
        int killer = (choose + 1) % 3;
            
        assert(verts[choose].size() && verts[killer].size());
        if (verts[choose].begin()->first != verts[killer].begin()->first) {
            return "IMPOSSIBLE";
        }
            
        auto fi = *verts[choose].begin();
        auto si = *verts[killer].begin();
            
        verts[choose].erase(verts[choose].begin());
        verts[killer].erase(verts[killer].begin());
        
        --cnt[choose];
        --ccnt[choose][fi.first];
        --ccnt[killer][si.first];
        ++ccnt[killer][si.first + 1];
        
        verts[killer].insert(Pos(si.first + 1, si.second, min(fi.res + si.res, si.res + fi.res)));
        
        last = killer;
        
        //cout << type[choose] << ' ' << type[killer] << ' ' << si.first << '\n';
    }
    
    return verts[last].begin()->res;
}

char win(char a, char b) {
    if (a == 'R' && b == 'P') return 'P';
    if (a == 'R' && b == 'S') return 'R';
    if (a == 'S' && b == 'R') return 'R';
    if (a == 'S' && b == 'P') return 'S';
    if (a == 'P' && b == 'R') return 'P';
    if (a == 'P' && b == 'S') return 'S';
    
    assert(false);
}

char play(int n, string const &res) {
    if (n + 1 >= res.size()) return res[n + 1 - res.size()];
    
    char left = play(2 * n + 1, res);
    char right = play(2 * n + 2, res);
    
    if (left == -1 || right == -1 || left == right) return -1;
    
    return win(left, right);
}


bool generate(int n, int r, int p, int s, string &res) {
    if (!r && !p && !s) {
        return play(0, res) != -1;
    }
    
    if (p) {
        res[n] = 'P';
        if (generate(n + 1, r, p - 1, s, res)) return true;
    }
    if (r) {
        res[n] = 'R';
        if (generate(n + 1, r - 1, p, s, res)) return true;
    }
    if (s) {
        res[n] = 'S';
        if (generate(n + 1, r, p, s - 1, res)) return true;
    }
    
    return false;
}


string stupid(int const n, int r, int p, int s) {
    string res(1 << n, ' ');
    
    if (!generate(0, r, p, s, res)) return "IMPOSSIBLE";
    
    return res;
}

void stress(int p) {
    for (int n = 1; n != p; ++n) {
        int total = 1 << n;
        
        for (int a = 0; a <= total; ++a) {
            for (int b = 0; a + b <= total; ++b) {
                solve(n, a, b, total - a - b);
            }
        }
    }
}


int main() {
    //freopen("/Users/iskhakovt/Downloads/A-small-attempt0.in", "r", stdin);
    //freopen("/Users/iskhakovt/out.txt", "w", stdout);
    
    int tests;
    cin >> tests;
    
    //stress(2);
    
    for (int t = 0; t != tests; ++t) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        string res = solve(n, r, p, s);
        
        if (res != "IMPOSSIBLE" && play(0, res) == -1) cout << "Case #" << t + 1 << " FAIL\n";
        
        cout << "Case #" << t + 1 << ": " << solve(n, r, p, s) << "\n";
    }
    
    return 0;
}
