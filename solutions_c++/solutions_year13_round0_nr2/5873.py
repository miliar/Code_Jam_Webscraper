#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n_cases;
    cin >> n_cases;

    for (int t = 1; t <= n_cases; t++) {
        int N, M;
        cin >> N >> M;
        vector<vector<short> > heights(N, vector<short>(M) );
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                cin >> heights[y][x];
            }
        }
        vector<short> max_xs(M);
        vector<short> max_ys(N);
        for (int x = 0; x < M; x++) {
            short max_value = 0;
            for (int y = 0; y < N; y++) {
                max_value = max(max_value, heights[y][x]);
            }
            max_xs[x] = max_value;
        }
        for (int y = 0; y < N; y++) {
            short max_value = 0;
            for (int x = 0; x < M; x++) {
                max_value = max(max_value, heights[y][x]);
            }
            max_ys[y] = max_value;
        }
        bool is_possible = true;
        for (int y = 0; y < N && is_possible; y++) {
            for (int x = 0; x < M && is_possible; x++) {
                if (heights[y][x] != min(max_xs[x], max_ys[y]) ) {
                    is_possible = false;
                }
            } 
        }
        cout << "Case #" << t << ": ";
        if (is_possible) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
