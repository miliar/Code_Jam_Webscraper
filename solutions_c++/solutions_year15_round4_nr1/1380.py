#include <cstdio>
#include <queue>

using namespace std;

int T;
int R, S;

int dr[] = {0, 1, 0, -1};
int ds[] = {1, 0, -1, 0};

int direction[256];

char grid[105][105];

queue <pair <int, int> > Q;

inline bool inside(int r, int s) {
    return r >= 0 && r < R && s >= 0 && s < S;
}

void solve(int t) {

    while (!Q.empty()) Q.pop();

    scanf("%d%d", &R, &S);
    for (int i = 0; i < R; ++i) {
        scanf("%s", grid[i]);
        for (int j = 0; j < S; ++j) {
            if (grid[i][j] != '.') Q.push(make_pair(i, j));
        }
    }

    int ret = 0;
    bool impossible = false;
    while (!Q.empty() && !impossible) {
        
        int r = Q.front().first, s = Q.front().second; Q.pop();
        int _r = r, _s = s;
        int found = 0;
        bool in_direction = false;

        for (int i = 0; i < 4; ++i) {
            r = _r; s = _s;
            while (inside(r + dr[i], s + ds[i])) {
                r += dr[i]; s += ds[i];
                if (grid[r][s] != '.') { 
                    if (i == direction[grid[_r][_s]]) in_direction = true;
                    ++found; break; 
                }
            }
        }
       
        impossible = found == 0;
        ret += !in_direction;

    }

    printf("Case #%d: ", t);
    if (impossible) printf("IMPOSSIBLE\n"); else printf("%d\n", ret);

}

int main(void) {

    direction['>'] = 0;
    direction['v'] = 1;
    direction['<'] = 2;
    direction['^'] = 3;
    
    scanf("%d", &T);
    for (int t = 0; t < T; ++t) solve(t + 1);

}
