#include <iostream>
#include <vector>
#include <string>

using namespace std;

const string arrow = "v>^<";
const int xdir[4] = {1, 0, -1, 0};
const int ydir[4] = {0, 1, 0, -1};

int solve_case();

int main() {
    int cases;
    cin >> cases;
    for (int round=1; round<=cases; round++) {
        int ans = solve_case();
        cout << "Case #" << round << ": ";
        if (ans < 0)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';
    }
}

int solve_case() {
    int r, c;
    scanf("%d%d", &r, &c);
    vector<string> data(r);
    for (string &s: data)
        cin >> ws >> s;
    int ans = 0;
    for (int x=0; x<r; x++)
        for (int y=0; y<c; y++) {
            char ch = data[x][y];
            auto curr_dir = arrow.find(ch);
            if (curr_dir == string::npos)
                continue;
            auto test_dir = [x, y, r, c, &data](int dir) {
                int curr_x = x, curr_y = y;
                auto shift = [&curr_x, &curr_y, dir]() {
                    curr_x += xdir[dir];
                    curr_y += ydir[dir];
                };
                auto in_range = [&curr_x, &curr_y, r, c]() {
                    return curr_x >= 0 && curr_y >= 0
                        && curr_x < r && curr_y < c;
                };
                shift();
                while (in_range()) {
                    if (data[curr_x][curr_y] != '.')
                        return true;
                    shift();
                }
                return false;
            };
            if (test_dir(curr_dir))
                continue;
            bool can_go = false;
            for (int i=0; i<4; i++)
                if (test_dir(i))
                    can_go = true;
            if (!can_go)
                return -1;
            else
                ans++;
        }
    return ans;
}
