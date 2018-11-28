#include <iostream>
#include <vector>
#include <deque>
#include <cstdio>
#include <climits>
#include <cstring>
using namespace std;

#define ll long long

int silly(int R, int C, vector<string>& G, int v) {
    int dx[] = {-1, 0, 1, 0};
    int dy[] = {0, -1, 0, 1};
    string D = "<^>v";

    if (v == R*C) {
        bool good = true;
        for (int r=0;r<R;++r) {
            for (int c=0;c<C;++c) {
                if (G[r][c] != '.') {
                    int d = D.find(G[r][c]);
                    int cr = r + dy[d], cc = c + dx[d];
                    bool good = false;
                    while (cr >=0 && cc >=0 && cr < R && cc < C) {
                        if (G[cr][cc] != '.') {
                            good = true;
                            break;
                        }
                        cr += dy[d];
                        cc += dx[d];
                    }
                    if (!good) { return -(1<<29); }
                }
                
            }
        }
        return 0;
    }

    int r = v /C;
    int c = v%C;
    
    if (G[r][c] == '.') {
        return silly(R, C, G, v+1);
    } else {
        int ans = silly(R, C, G, v+1);
        if (ans >= 0) {
            return ans;
        }

        int d = D.find(G[r][c]);
        for (int i=0;i<4;++i) {
            if (i == d) continue;
            G[r][c] = D[i];
            ans = silly(R, C, G, v+1);
            if (ans >= 0) {
                return ans + 1;
            }
        }

        G[r][c] = D[d];
    }
    
    return -(1<<29);
}

int main() {
    int T;
    cin>>T;

    for (int t=1;t<=T;++t) {
        int R, C;
        cin>>R>>C;
        vector<string> G;
        for (int i=0;i<R;++i) {
            string s;
            cin>>s;
            G.push_back(s);
        }



        vector<int> ra[100], ca[100];

        for (int r=0;r<R;++r) {
            for (int c=0;c<C;++c) {
                if (G[r][c] != '.') {
                    ra[r].push_back(c);
                    ca[c].push_back(r);
                }
            }
        }

        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        string D = "<^>v";

        bool impossible = false;
        int ans = 0;

        for (int r=0;r<R;++r) {
            for (int c=0;c<C;++c) {
                char gd = G[r][c];
                if (gd != '.') {
                    int d = D.find(gd);
                    if (ra[r].size() == 1 && ca[c].size() == 1) {
                        impossible = true;
                        r = R;
                        break;
                    }

                    int cr = r + dy[d], cc = c + dx[d];
                    bool good = false;
                    while (cr >=0 && cc >=0 && cr < R && cc < C) {
                        if (G[cr][cc] != '.') {
                            good = true;
                            break;
                        }
                        cr += dy[d];
                        cc += dx[d];
                    }

                    if (!good) {
                        ans++;
                    }
                }
            }
        }
        /*
        int sl = silly(R, C, G, 0);
        if (sl < 0) sl = -1;
        */

        if (impossible) {
            ans = -1;
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }

/*
        if (ans != sl) {
            printf("!!!!!!! %d vs %d\n", ans, sl);
        }
        */
    }
}
