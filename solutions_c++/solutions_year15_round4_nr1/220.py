#include <fstream>

using namespace std;

const int MAXN = 105;
int gox[] = {-1, 0, 1, 0}, goy[] = {0, -1, 0, 1};
char c[MAXN][MAXN];

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int n, m;
        in >> n >> m;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                in >> c[i][j];
        int ans = 0, impossible = false;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++) {
                if(c[i][j] == '.')
                    continue;
                int x = i, y = j, dir = (c[i][j] == '^'? 0 :
                                         (c[i][j] == '<'? 1 :
                                          (c[i][j] == 'v'? 2 : 3)));
                while(true) {
                    x = x + gox[dir];
                    y = y + goy[dir];
                    if(x < 0 || x >= n || y < 0 || y >= m || c[x][y] != '.')
                        break;
                }
                if(x < 0 || x >= n || y < 0 || y >= m) {
                    bool bad = true;
                    for(dir = 0; dir < 4; dir++) {
                        x = i;
                        y = j;
                        while(true) {
                            x = x + gox[dir];
                            y = y + goy[dir];
                            if(x < 0 || x >= n || y < 0 || y >= m || c[x][y] != '.')
                                break;
                        }
                        if(x < 0 || x >= n || y < 0 || y >= m)
                            continue;
                        bad = false;
                        break;
                    }
                    if(bad)
                        impossible = true;
                    ans++;
                }
            }
        out << "Case #" << tt + 1 << ": ";
        if(impossible)
            out << "IMPOSSIBLE\n";
        else
            out << ans << '\n';
    }
    return 0;
}
