#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>

using namespace std;

vector< vector< int > > ind;
vector< int > g, cnt;
vector< vector< char > > field;
int r, c;
int counter;

const map< char, int > DX = {{'^', -1}, {'v', 1}, {'>', 0}, {'<', 0}};
const map< char, int > DY = {{'^', 0}, {'v', 0}, {'>', 1}, {'<', -1}};

bool
is_border(int n, int x)
{
    return (0 <= x && x < n);
}

int
next_val(int x, int y)
{
    int dx = DX.at(field[x][y]), dy = DY.at(field[x][y]);
    do {
        x += dx, y += dy;
    } while (is_border(r, x) && is_border(c, y) && field[x][y] == '.');
    if (is_border(r, x) && is_border(c, y)) {
        return ind[x][y];
    }
    return -1;
}

bool
process(int id)
{
    if (!(cin >> r >> c)) {
        return false;
    }
    ind.assign(r, vector< int >(c, -1));
    field.assign(r, vector< char >(c, '.'));
    counter = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            char cur_c;
            cin >> cur_c;
            //cerr << cur_c;
            field[i][j] = cur_c;
            if (cur_c != '.') {
                ind[i][j] = counter++;
            }
        }
        //cerr << endl;
    }
    g.assign(counter, -1);
    cnt.assign(counter, 0);
    cout << "Case #" << id << ": ";
    int res = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (field[i][j] == '.') {
                continue;
            }
            int sum_add = -1;
            for (char go : {'>', '<', 'v', '^'}) {
                char old_chr = field[i][j];
                field[i][j] = go;
                if (next_val(i, j) != -1) {
                    int cur = (old_chr != go);
                    if (sum_add == -1 || sum_add > cur) {
                        sum_add = cur;
                    }
                }
                field[i][j] = old_chr;
            }
            if (sum_add == -1) {
                cout << "IMPOSSIBLE\n";
                return true;
            }
            res += sum_add;
        }
    }
    cout << res << '\n';
    return true;
}

int
main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        process(i);
    }
    return 0;
}
