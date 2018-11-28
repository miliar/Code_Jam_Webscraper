#include <cstdio>
#include <queue>
#define MAX_DIM 5
#define MAX_MINES 24

int dx[] = {0,1,1,1,0,-1,-1,-1};
int dy[] = {-1,-1,0,1,1,1,0,-1};

int try_grid(int grid);
void print_grid();

int r,c,m;
int n_tasks;

using namespace std;

int main() {
    scanf("%d", &n_tasks);
    for (int t = 1; t <= n_tasks; t++) {
        scanf("%d %d %d", &r, &c, &m);
        printf("Case #%d:\n", t);
        
        int worked = 0;
        for (int i = 0; i < (1 << r*c); i++) {
            if (__builtin_popcount(i) != m) continue;
            if (try_grid(i)) {
                print_grid();
                worked = 1;
                break;
            }
        }
        if (!worked) {
            printf("Impossible\n");
        }
    }
    
    
    return 0;
}

int gar[MAX_DIM][MAX_DIM];
int term[MAX_DIM][MAX_DIM];
int seen[MAX_DIM][MAX_DIM];
int cx, cy;
queue<pair<int,int> > st;
int try_grid(int grid) {
    int i = 0;
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            term[y][x] = 0;
        }
    }
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            gar[y][x] = (grid & (1<<i)) ? 1 : 0;
            if (gar[y][x]) {
                term[y][x] = 1;
            }
            if (gar[y][x]) {
                for (int d = 0; d < 8; d++) {
                    if (x+dx[d] < c && x+dx[d] >= 0 &&
                        y+dy[d] < r && y+dy[d] >= 0) {
                        term[y+dy[d]][x+dx[d]] = 1;
                    }
                }
            }
            i++;
        }
    }
    int did = 0;
    int non_gar = 0;
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            if (!term[y][x]) {
                cx = x;
                cy = y;
                did = 1;
                break;
            }
            if (!gar[y][x]) {
                cx = x;
                cy = y;
                non_gar++;
            }
        }
        if (did) {
            break;
        }
    }
    if (!did) {
        if (non_gar == 1) {
            return 1;
        } else {
            return 0;
        }
    } else {
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                seen[y][x] = 0;
            }
        }
        int found = 0;
        st.push(pair<int,int>(cy,cx));
        seen[cy][cx] = 1;
        while (!st.empty()) {
            pair<int,int> cur = st.front();
            found++;
            st.pop();
            int y = cur.first;
            int x = cur.second;
            if (term[y][x]) continue;
            for (int d = 0; d < 8; d++) {
                if (x+dx[d] < c && x+dx[d] >= 0 &&
                    y+dy[d] < r && y+dy[d] >= 0) {
                    if (!gar[y+dy[d]][x+dx[d]] &&
                        !seen[y+dy[d]][x+dx[d]]) {
                        st.push(pair<int,int>(y+dy[d],x+dx[d]));
                        seen[y+dy[d]][x+dx[d]] = 1;
                    }
                }
            }
        }
        if (r*c-found == m) {
            return 1;
        } else {
            return 0;
        }
    }
}

void print_grid() {
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            if (x == cx && y == cy) {
                putchar('c');
            } else if (gar[y][x]) {
                putchar('*');
            } else {
                putchar('.');
            }
        }
        putchar('\n');
    }
}
