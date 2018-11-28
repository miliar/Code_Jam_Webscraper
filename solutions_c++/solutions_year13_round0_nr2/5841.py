#include<iostream>
#include<vector>
#include<set>
using namespace std;

bool cut_single_square(vector<vector<int>> &H, int n, int m) {
    bool possible = true;
    for (int j = 0; j < H[0].size(); ++j) {
        if (H[n][j] > H[n][m]) {
            possible = false;
            break;
        }
    }
    if (possible) return true;
    possible = true;
    for (int i = 0; i < H.size(); ++i) {
        if (H[i][m] > H[n][m]) {
            possible = false;
            break;
        }
    }
    return possible;
}

bool cut_next_level(vector<vector<int>> &H, int cur_height) {
    for (int i = 0; i < H.size(); ++i) {
        for(int j = 0; j < H[0].size(); ++j) {
            if (H[i][j] == cur_height && !cut_single_square(H,i,j))
                return false;
        }
    }
    return true;
}

int main() {
    int T,N,M,h;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> M;
        vector<vector<int>> height(N, vector<int>(M));
        set<int> known_heights;
        for (int i = 0; i < N; ++i) for (int j = 0; j < M; ++j) {
            cin >> height[i][j];
            known_heights.insert(-height[i][j]);
        }
        bool possible = true;
        for (auto it : known_heights) {
            if (!cut_next_level(height,-it)) {
                possible = false;
                break;
            }
        }
        cout << "Case #" << t << ": " << (possible ? "YES" : "NO") << endl;
    }
    return 0;
}
