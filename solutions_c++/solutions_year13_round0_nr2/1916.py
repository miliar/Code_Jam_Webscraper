#include <iostream>
#include <cstdio>
#include <vector>

using std::vector;

vector <bool> check_rows, check_cols;

unsigned get_row(vector < vector<int> > const & A, int cur_min) {
    for(int i = 0; i < A.size(); ++i) {
        if(check_rows[i])
            continue;
        bool valid = true;
        for(int j = 0; j < A[0].size(); ++j)
            if(A[i][j] != cur_min && A[i][j] != 0) {
                valid = false;
                break;
            }
        if(valid) {
            check_rows[i] = true;
            return i;
        }
    }
    return -1;
}

unsigned get_col(vector < vector<int> > const & A, int cur_min) {
    for(int i = 0; i < A[0].size(); ++i) {
        if(check_cols[i])
            continue;
        bool valid = true;
        for(int j = 0; j < A.size(); ++j)
            if(A[j][i] != cur_min && A[j][i] != 0) {
                valid = false;
                break;
            }
        if(valid) {
            check_cols[i] = true;
            return i;
        }
    }
    return -1;
}

using std::cin;
using std::cout;
using std::endl;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        int n, m;
        cin >> n >> m;
        vector < vector <int> > A(n, vector <int> (m));
        check_cols.resize(m);
        check_cols.assign(m, false);
        check_rows.resize(n);
        check_rows.assign(n, false);
        vector <int> B(101);
        int cur_min = 100;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j) {
                cin >> A[i][j];
                B[A[i][j]]++;
                if(A[i][j] < cur_min)
                    cur_min = A[i][j];
            }

        int c = 0;
        while(cur_min <= 100 && c != -1) {
            c = get_row(A, cur_min);
            if(c != -1) {
                for(int i = 0; i < m; ++i) {
                    if(B[A[c][i]])
                        B[cur_min]--;
                    A[c][i] = 0;
                }
                while(cur_min <= 100 && B[cur_min] == 0)
                    ++cur_min;
                continue;
            }
            c = get_col(A, cur_min);
            if(c != -1) {
                for(int i = 0; i < n; ++i) {
                    if(B[A[i][c]])
                        B[cur_min]--;
                    A[i][c] = 0;
                }
                while(cur_min <= 100 && B[cur_min] == 0)
                    ++cur_min;
                continue;
            }
        }
        cout << "Case #" << t << ": ";
        if(c == -1)
            cout << "NO\n";
        else
            cout << "YES\n";

    }
    return 0;
}
