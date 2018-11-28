#include <vector>
#include <cmath>
#include <cstdio>
#include <list>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <stack>
#include <map>
#include <iostream>
#include <string>
#include <set>

using namespace std;
void print_matrix(vector<vector<char> > &mat, int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j)
            cout << mat[i][j];
        cout << endl;
    }
}

int dx[] = {0, 0,  1, -1, -1, 1, -1, 1};
int dy[] = {1, -1, 0, 0,  -1, 1, 1, -1};

bool is_in(int x, int y, int r, int c) {
    return (x >= 0 && x < r && y >= 0 && y < c);
}

bool dfs(vector<vector<char> > &mat, int r, int c, int n, int x, int y) {
    if (n == 0)
        return true;

    if (n < 0)
        return false;

    vector<pair<int, int> > vec;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (is_in(nx, ny, r, c) && mat[nx][ny] == '*')
            vec.push_back(make_pair(nx,ny));
    }

    if (vec.size() > n)
        return false;

    for (int i = 0; i < vec.size(); ++i) {
        int nx = vec[i].first;
        int ny = vec[i].second;
        mat[nx][ny] = '.';
    }

    for (int i = 0; i < vec.size(); ++i) {
        int nx = vec[i].first;
        int ny = vec[i].second;
        if (dfs(mat, r, c, n-vec.size(), nx, ny))
            return true;
    }

    // recover
    for (int i = 0; i < vec.size(); ++i) {
        int nx = vec[i].first;
        int ny = vec[i].second;
        mat[nx][ny] = '*';
    }

    return false;
}

bool dfs_helper(vector<vector<char> > &mat, int r, int c, int n) {
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j) {
            mat[i][j] = 'c';
            if (dfs(mat, r, c, n-1, i, j))
                return true;
            mat[i][j] = '*';
        }

    return false;
}

void func() {
    int r,c,m;
    cin >> r >> c >> m;

    vector<vector<char> > mat(r, vector<char>(c, '*'));

    if (m+1 == r*c) {
        mat[0][0] = 'c';
        print_matrix(mat, r, c);
        return;
    }
        
    if (r == 1) {
        mat[0][0] = 'c';
        for (int i = 1; i < r*c-m; ++i)
            mat[0][i] = '.';
        print_matrix(mat, r, c);
        return;
    }

    if (c == 1) {
        mat[0][0] = 'c';
        for (int i = 1; i < r*c-m; ++i)
            mat[i][0] = '.';
        print_matrix(mat, r,c);
        return;
    }

    bool ret = dfs_helper(mat, r, c, r*c-m);
    if (ret)
        print_matrix(mat, r, c);
    else
        cout << "Impossible" << endl;
}


//////////////////////////////

char in_file[] = "C-small-attempt2.in";
char out_file[] = "test.out";

int main() {
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    for (t = 1; t <= case_count; t++) {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ":\n";
        func();
    }

	return 0;    
}
