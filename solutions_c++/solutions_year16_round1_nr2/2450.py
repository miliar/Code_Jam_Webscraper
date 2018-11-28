#include <iostream>
#include <string>
#include <sstream>
#include <vector>


using namespace std;
struct Res {
    int col;
    int row;
};
void print_m(vector<vector<int> > &m) {
    for (int i= 0; i < m.size(); ++i) {
        for (int  j= 0; j < m[i].size(); ++j) {
            cerr << " " << m[i][j];
        }
        cerr << endl;
    }
}
Res solve(vector<bool> &used_row, vector<bool> &used_col, vector<vector<int> > &m, vector<vector<int> > &input, vector<bool> &used_input, int index) {
    if (used_input[index]) {
        return solve(used_row, used_col, m, input, used_input, index + 1);
    }
    if (index >= input.size()) {
        Res r;
        r.col = -1;
        r.row = -1;
        for (int i = 0; i < used_col.size(); ++i) {
            if (!used_col[i]) {
                r.col = i;
                return r;
            }
        }
        for (int i = 0; i < used_row.size(); ++i) {
            if (!used_row[i]) {
                r.row = i;
                return r;
            }
        }

        // Error
        cerr  << "no unused" << endl;
        return r;
    }

    // find row
    {
        int row = -1;
        for (int i = 0; i < m.size(); ++i ) {
            if (used_row[i]) continue;
            if ((m[i][0] == -1 || m[i][0] == input[index][0])
                 && (m[i].back() == -1 || m[i].back() == input[index].back())) {
                row = i;
                break;
            }
        } 
        if (row != -1) {
            vector<int> saved;
            bool restore = false;
            for (int i = 0; i < m.size(); ++i) {
                saved.push_back(m[row][i]);
                if (m[row][i] == -1 || m[row][i] == input[index][i]) {
                    m[row][i] = input[index][i];
                } else {
                    restore = true;
                    break;

                }
            }
            // swap(m[row], input[index]);
            if (!restore) {
                used_row[row] = true;
                Res r = solve(used_row, used_col, m, input, used_input, index+1);
                if (r.row != -1 || r.col != -1) {
                    return r;
                }
            }
            used_row[row] = false;
            for (int i = 0; i < saved.size(); ++i) {
                m[row][i] = saved[i];
            }
            // swap(m[row], input[index]);
        }
    }
    // find col
    {
        int col = -1;
        for (int i = 0; i < m.size(); ++i ) {
            if (used_col[i]) continue;
            if ((m[0][i] == -1 || m[0][i] == input[index][0])
                 && (m.back()[i] == -1 || m.back()[i] == input[index].back())) {
                col = i;
                break;
            }
        } 
        if (col != -1) {
            vector<int> saved;
            bool restore = false;
            for (int i = 0; i < m.size(); ++i) {
                saved.push_back(m[i][col]);
                if (m[i][col] == -1 || m[i][col] == input[index][i]) {
                    m[i][col] = input[index][i];
                } else {
                    restore = true;
                    break;

                }
            }
            if (!restore) {
                used_col[col] = true;
                Res r = solve(used_row, used_col, m, input, used_input, index+1);
                if (r.row != -1 || r.col != -1) {
                    return r;
                }
            }
            used_col[col] = false;
            for (int i = 0; i < saved.size(); ++i) {
                m[i][col] = saved[i];
            }
        }
    }

    // no solution
    Res r;
    r.col = -1;
    r.row = -1;
    return r;
}

int main() {
    int T;
    cin >>T;
    for (int t = 0 ;t < T; ++t) {
        int N;
        cin >> N;
        vector<int> dummy(N, -1);
        vector<bool> used_col(N, false);
        vector<bool> used_row(N, false);
        vector<vector<int> > m(N, dummy);
        vector<vector<int> > input;
        vector<bool> used_input(2*N-1, false);
        int min = 2501;
        vector<int> min_vector;
        int max = -1;
        vector<int> max_vector;
        for (int i = 0; i < 2*N-1; ++i) {
            vector<int> current;
            for (int j = 0; j < N; ++j) {
                int t; 
                cin >> t;
                current.push_back(t);
            }
            if (current[0] < min) {
                min = current[0];
                min_vector.clear();
            }
            if (current[0] == min && min_vector.size() < 2) {
                min_vector.push_back(input.size());
            }
            if (current.back() > max) {
                max = current.back();
                max_vector.clear();
            }
            if (current.back() == max && max_vector.size() < 2) {
                max_vector.push_back(input.size());
            }
            input.push_back(current);
        }
        if (min_vector.size() == 2) {
            for (int i = 0; i < N; ++i) {
                m[0][i] = input[min_vector[0]][i];
            }
            for (int i = 0; i < N; ++i) {
                m[i][0] = input[min_vector[1]][i];
            }
            used_row[0] = true;
            used_col[0] = true;
            used_input[min_vector[0]] = true;
            used_input[min_vector[1]] = true;
        }
        if (max_vector.size() == 2) {

            if (m[N-1][0] == -1 || m[N-1][0] == input[max_vector[0]][0]) {
                for (int i = 0; i < N; ++i) {
                    m[N-1][i] = input[max_vector[0]][i];
                }
                for (int i = 0; i < N; ++i) {
                    m[i][N-1] = input[max_vector[1]][i];
                }
            } else {
                for (int i = 0; i < N; ++i) {
                    m[N-1][i] = input[max_vector[1]][i];
                }
                for (int i = 0; i < N; ++i) {
                    m[i][N-1] = input[max_vector[0]][i];
                }
            }


            used_row[N-1] = true;
            used_col[N-1] = true;
            used_input[max_vector[0]] = true;
            used_input[max_vector[1]] = true;
        }
        Res r = solve(used_row, used_col, m, input, used_input, 0);
        cout << "Case #" << t+1 << ":";
        if (r.col != -1) {
            for (int i = 0; i < m.size(); i++) {
                cout << " " << m[i][r.col];
            }
            cout << endl;
            continue;
        }
        if (r.row != -1) {
            for (int i = 0; i < m.size(); i++) {
                cout << " " << m[r.row][i];
            }
            cout << endl;
            continue;
        }
        

    }
    return 0;

}
