#include <iostream>
#include <cassert>
#include <map>
#include <vector>

using namespace std;

map<int, int> m;


int R, C, T;

bool h[200][200];
int aht[200][200];
struct pos {
    int r, c;
};

int run(pos last, pos cur) {
    if(aht[cur.r][cur.c]) {
        return aht[cur.r][cur.c];
    }
    vector<pos> c1;
    vector<pos> c2;
    if(h[cur.r][cur.c]) {
        // /
        c1.push_back({cur.r-1, cur.c});
        c2.push_back({cur.r, cur.c-1});
        c1.push_back({cur.r+1, cur.c});
        c2.push_back({cur.r, cur.c+1});
    } else {
        // backslash
        c1.push_back({cur.r+1, cur.c});
        c2.push_back({cur.r, cur.c-1});
        c1.push_back({cur.r, cur.c+1});
        c2.push_back({cur.r-1, cur.c});
    }
    if(c1[0].r == last.r && c1[0].c == last.c) {
        return run(cur, c2[0]);
    }
    if(c1[1].r == last.r && c1[1].c == last.c) {
        return run(cur, c2[1]);
    }
    if(c2[0].r == last.r && c2[0].c == last.c) {
        return run(cur, c1[0]);
    }
    if(c2[1].r == last.r && c2[1].c == last.c) {
        return run(cur, c1[1]);
    }
    assert(false);
}


bool works() {
    //cerr << "Try this\n";
            for(int r = 1; r <= R; r++) {
                for(int c = 1; c <= C; c++) {
                    //cerr << (h[r][c] ? "/" : "\\");
                }
                //cerr << "\n";
            }
    vector<pos> pas;
    for(int j = 1; j <= C; j++) {
        // u
        int me = aht[0][j];
        pos at = {0, j};
        int you = run(at, {1, j});
        pas.push_back({me, you});
        //cerr << me << " connects to " << you << "\n";
    }
    for(int j = 1; j <= C; j++) {
        // d
        int me = aht[R+1][j];
        pos at = {R+1, j};
        int you = run(at, {R, j});
        pas.push_back({me, you});
        //cerr << me << " connects to " << you << "\n";
    }
    for(int j = 1; j <= R; j++) {
        // l
        int me = aht[j][0];
        pos at = {j, 0};
        int you = run(at, {j, 1});
        pas.push_back({me, you});
        //cerr << me << " connects to " << you << "\n";
    }
    for(int j = 1; j <= R; j++) {
        // r
        int me = aht[j][C+1];
        pos at = {j, C+1};
        int you = run(at, {j, C});
        pas.push_back({me, you});
        //cerr << me << " connects to " << you << "\n";
    }
    for(int i = 0; i < pas.size(); i++) {
        pos cur = pas[i];
        //cerr <<"Compare " << "m[" << cur.r << "]" << m[cur.r] << " " << cur.c << "\n";
        if(m[cur.r] != cur.c) {
            return false;
        }
    }
    return true;
}

bool att() {
    //cerr << "Attention\n";
    for(int b = 0; b < (1<<(R*C)); b++) {
        int i = 0;
        for(int r = 1; r <= R; r++) {
            for(int c = 1; c <= C; c++) {
                h[r][c] = (b & (1<<i));
                i++; 
            }
        }
        if(works()) {
            return true;
        }
    }
    return false;
}

void maht() {
    int i = 1;
    for(int j = 1; j <= C; j++) {
        aht[0][j] = i;
        i++;
    }
    for(int j = 1; j <= R; j++) {
        aht[j][C+1] = i;
        i++;
    }
    for(int j = C; j >= 1; j--) {
        aht[R+1][j] = i;
        i++;
    }
    for(int j = R; j >= 1; j--) {
        aht[j][0] = i;
        i++;
    }
}

int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cerr << "Case " << t << "\n";
        cin >> R >> C;
        for(int r = 0; r <= R; r++) {
            for(int c = 0; c <= C; c++) {
                aht[r][c] = 0;
            }
        }
        maht();
        for(int r = 0; r <= R+1; r++) {
            for(int c = 0; c <= C+1; c++) {
                //cerr << aht[r][c];
            }
            //cerr << "\n";
        }
        m.clear();
        for(int i = 1; i <= (R+C); i++) {
            int x, y;
            cin >> x >> y;
            //cerr << "Pair " << x << " " << y << "\n";
            m[x] = y;
            m[y] = x;
        }
        cout << "Case #" << t << ":\n";
        if(att()) {
            for(int r = 1; r <= R; r++) {
                for(int c = 1; c <= C; c++) {
                    cout << (h[r][c] ? "/" : "\\");
                }
                cout << "\n";
            }
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
