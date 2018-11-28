#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool compare(vector<vector<int> > &m1, vector<vector<int> > &m2, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (m1[i][j] != m2[i][j]) return false;
        }
    }

    return true;
}

int get_row_max(vector<vector<int> > &lawn, int m, int n, int row) {
    int maxx = lawn[row][0];

    for (int j = 1; j < n; j++) {
        maxx = max(maxx, lawn[row][j]);
    }

    return maxx;
}

int get_col_max(vector<vector<int> > &lawn, int m, int n, int col) {
    int maxx = lawn[0][col];

    for (int i = 1; i < m; i++) {
        maxx = max(maxx, lawn[i][col]);
    }

    return maxx;
}

string magia(vector<vector<int> > &lawn, int m, int n) {
    vector<vector<int> > aux_lawn(m, vector<int>(n,100));
    vector<int> row_max(m), col_max(n);

    for (int i = 0; i < m; i++) {
        row_max[i] = get_row_max(lawn, m, n, i);
    }
    for (int j = 0; j < n; j++) {
        col_max[j] = get_col_max(lawn, m, n, j);
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            aux_lawn[i][j] = min(row_max[i], col_max[j]);
        }
    }

    if (compare(lawn, aux_lawn, m, n))
        return "YES";
    else
        return "NO";
}

int main() {
    int t;
    int m, n;
    vector<vector<int> > lawn;

    cin >> t;
    for (int no_case = 1; no_case <= t; no_case++) {
        cin >> m >> n;

        lawn.clear();
        lawn.resize(m, vector<int>(n));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> lawn[i][j];
            }
        }

        cout << "Case #" << no_case << ": " << magia(lawn, m, n) << endl;
    }

    return 0;
}
