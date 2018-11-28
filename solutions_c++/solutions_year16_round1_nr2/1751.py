#include <cassert>
#include <cmath>
#include <cstdint>
#include <bitset>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int T, N, v;
int height[50][50];
int rows[50];
int cols[50];
vector<vector<int>> lines;
map<int, int> counts;

void add_line(vector<int> line) {
    int i = 0;
    vector<vector<int>>::iterator it = lines.begin();
    while (i < lines.size()) {
        for (int j = 0; j < N; ++j) {
            if (lines[i][j] > line[j]) {
                lines.insert(it, line);
                return;
            }
        }
        ++i;
        ++it;
    }
    lines.insert(it, line);
}

void put_line(vector<int> line) {
    for (int i = 0; i < N; ++i) {
        if (height[0][i] == line[i]) {
            cols[i] = 1;
            for (int j = 0; j < N; ++j) {
                height[j][i] = line[j];
            }
            return;
        }
        else if (height[i][0] == 0) {
            rows[i] = 1;
            for (int j = 0; j < N; ++j)
                height[i][j] = line[j];
            return;
        }
    }

    int i = 0;
    while (i < N) {
        if (height[i][0] == line[0]) {
            cols[i] = 1;
            for (int j = 0; j < N; ++j) {
                height[j][i] = line[j];
            }
                
            return;
        }

        if (height[i][0] == 0) {
            rows[i] = 1;
            for (int j = 0; j < N; ++j)
                height[i][j] = line[j];
            return;
        }
        ++i;
    }
}

void solve() {
    for (int i = 0; i < N; ++i) {
        rows[i] = cols[i] = 0;
        for (int j = 0; j < N; ++j) {
            height[i][j] = 0;
        }
    }

    for (int i = 0; i < 2 * N - 1; ++i) {
        put_line(lines[i]);
    }

    for (int i = 0; i < N; ++i) {
        if (rows[i] == 0) {
            for (int j = 0; j < N; ++j)
                cout << height[i][j] << " ";
            break;
        }
        else if (cols[i] == 0) {
            for (int j = 0; j < N; ++j)
                cout << height[j][i] << " ";
            break;
        }
    }
    cout << endl;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        lines.clear();
        counts.clear();

        for (int i = 0; i < 2 * N - 1; ++i) {
            vector<int> line;
            for (int j = 0; j < N; ++j) {
                cin >> v;
                line.push_back(v);

                if (counts.count(v) == 0) counts[v] = 1;
                else counts[v] = counts[v] + 1;
            }
            add_line(line);
        }

        cout << "Case #" << t << ": ";
        //solve();

        vector<int> res;
        for (map<int, int>::iterator it = counts.begin(); it != counts.end(); ++it) {
            if (it->second % 2 == 1) 
                res.push_back(it->first);
        }
        sort(res.begin(), res.end());
        for (auto value : res)
            cout << value << " ";
        cout << endl;
    }
    return 0;
}