#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

map<char, int> dx{{'<', 0}, {'^', -1}, {'>', 0}, {'v', 1}};
map<char, int> dy{{'<', -1}, {'^', 0}, {'>', 1}, {'v', 0}};
char dir[] = "<^>v";

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        int N, M; cin >> N >> M;

        vector<string> S(N);
        for (int i = 0; i < N; ++i)
            cin >> S[i];

        vector< vector<int> > A(N, vector<int>(M, -1));
        int nodes = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                if (S[i][j] != '.')
                    A[i][j] = nodes++;
        bool impossible = false;
        int answer = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                if (S[i][j] != '.') {
                    auto good = [&](int x, int y) {
                        return x >= 0 && x < N && y >= 0 && y < M;
                    };
                    auto move = [&](char direction) {
                        int x = i;
                        int y = j;
                        do {
                            x += dx[direction];
                            y += dy[direction];
                        } while (good(x, y) && S[x][y] == '.');
                        return make_pair(x, y);
                    };

                    int x, y;
                    tie(x, y) = move(S[i][j]);
                    if (good(x, y))
                        continue;
                    bool found = false;
                    for (int i = 0; i < 4; ++i) {
                        tie(x, y) = move(dir[i]);
                        if (good(x, y)) {
                            found = true;
                            break;
                        }
                    }
                    if (!found)
                        impossible = true;
                    ++answer;
                }
        cout << "Case #" << test << ": ";
        if (impossible)
            cout << "IMPOSSIBLE\n";
        else
            cout << answer << "\n";
    }
}
