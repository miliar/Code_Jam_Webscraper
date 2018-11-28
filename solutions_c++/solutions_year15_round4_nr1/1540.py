#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <utility>
using namespace std;

typedef pair<int, int> Pair;
vector<Pair> arrows;

int r;
int c;
int T;
bool imp;
char field[100][100];
bool used[100][100];
bool is_arrow[100][100];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int rec(int x, int y, char dir, int count) {
    int dx;
    int dy;
    int savex;
    int savey;

    if (used[y][x]) return 0;
    used[y][x] = true;

    if (dir == '^') {
        dx = 0;
        dy = -1;
    } else if (dir == '>') {
        dx = 1;
        dy = 0;
    } else if (dir == '<') {
        dx = -1;
        dy = 0;
    } else if (dir == 'v') {
        dx = 0;
        dy = 1;
    } else assert(0);

    savex = x;
    savey = y;
    while (1) {
        x += dx;
        y += dy;

        if (x < 0 || c <= x) {
            if (count > 1) return 1;
            else if (count == 1) {
                used[savey][savex] = false;
                return -1;
            }
            else assert(0);
        }
        if (y < 0 || r <= y) {
            if (count > 1) return 1;
            else if (count == 1) {
                used[savey][savex] = false;
                return -1;
            }
            else assert(0);
        }
    
        if (field[y][x] != '.') return rec(x, y, field[y][x], count+1); 
    }
}

int main() {
    scanf("%d", &T);
    for (int Case=1; Case<=T; Case++) {
        int ans = 0;
        arrows.clear();
        memset(used, 0, sizeof(used));
        memset(is_arrow, 0, sizeof(is_arrow));
        imp = false;

        scanf("%d %d", &r, &c);
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                scanf(" %c", &field[i][j]);
                if (field[i][j] != '.') {
                    arrows.push_back(Pair(i, j));
                    is_arrow[i][j] = true;
                }
            }
        }

        for (int i=0; i<arrows.size(); i++) {
            int x = arrows[i].second;
            int y = arrows[i].first;

            if (!used[y][x]) {
                int ret;
                ret = rec(x, y, field[y][x], 1);
                if (ret != -1) {
                    ans += ret;
                }
            }
        }

        for (int i=0; i<arrows.size(); i++) {
            int x = arrows[i].second;
            int y = arrows[i].first;

            if (!used[y][x]) {
                for (int j=0; j<4 && !used[y][x]; j++) {
                    int newx = x + dx[j];
                    int newy = y + dy[j];

                    while (1) {
                        if (newx < 0 || c <= newx) break;
                        if (newy < 0 || r <= newy) break;

                        if (is_arrow[newy][newx]) {
                            used[y][x] = true;
                            ans++;
                            break;
                        }

                        newx += dx[j];
                        newy += dy[j];
                    }   
                }

                if (!used[y][x]) {
                    imp = true;
                    break;
                }
            }
        }

        if (imp) {
            printf("Case #%d: IMPOSSIBLE\n", Case);
            continue;
        }

        printf("Case #%d: %d\n", Case, ans);
    }
}
