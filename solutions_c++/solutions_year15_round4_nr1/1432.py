#include<iostream>
#include<vector>
#define r first
#define c second
using namespace std;
typedef pair<int, int> Point;
const int BUF = 105;


const string dirStr = "^>v<";
const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};

int row, col;
char b[BUF][BUF];

void read() {
    cin >> row >> col;
    for (int i = 0; i < row; ++i)
        for (int j = 0; j < col; ++j)
            cin >> b[i][j];
}


void dfs(int r, int c, int dir, bool visited[BUF][BUF], vector<Point> &order) {
    int nexDir = dir;
    if (b[r][c] != '.') {
        visited[r][c] = true;
        nexDir = dirStr.find(b[r][c]);
    }

    int nr = r + dr[nexDir];
    int nc = c + dc[nexDir];
        
    if (0 <= nr && nr < row && 0 <= nc && nc < col && !visited[nr][nc]) {
        dfs(nr, nc, nexDir, visited, order);
    }
    
    if (b[r][c] != '.') {
        order.push_back(make_pair(r, c));
    }
}


void work(int cases) {
    vector<Point> order;
    bool visited[BUF][BUF] = {};
    
    for (int i = 0; i < row; ++i)
        for (int j = 0; j < col; ++j) {
            if (b[i][j] == '.') continue;
            if (visited[i][j]) continue;
            
            int dir = dirStr.find(b[i][j]);
            
            dfs(i, j, dir, visited, order);
        }

    //for (int i = 0; i < order.size(); ++i)
    //    cout << order[i].first << ',' << order[i].second << endl;

    int cnt = 0;
    for (int i = 0; i < order.size(); ++i) {
        Point &pt = order[i];
        
        int dir = dirStr.find(b[pt.r][pt.c]);
        int r = pt.r;
        int c = pt.c;
        while (1) {
            r += dr[dir];
            c += dc[dir];
            if (0 <= r && r < row && 0 <= c && c < col && b[r][c] != '.') {
                goto _isOk;
            }
            if (!(0 <= r && r < row && 0 <= c && c < col))
                break;
        }

        ++cnt;

        for (int j = 0; j < 4; ++j) {
            int rr = pt.r;
            int cc = pt.c;
            while (1) {
                rr += dr[j];
                cc += dc[j];
                if (0 <= rr && rr < row && 0 <= cc && cc < col && b[rr][cc] != '.') {
                    goto _isOk;
                }
                if (!(0 <= rr && rr < row && 0 <= cc && cc < col)) {
                    break;
                }
            }
        }
        
        cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        return;
        
    _isOk:;
    }

    cout << "Case #" << cases << ": " << cnt << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
