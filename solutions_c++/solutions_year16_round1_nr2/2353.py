#include <algorithm>
#include <cstdio>
#include <iostream>


using namespace std;
typedef long long ll;

int N;
int M;
int rows[100];
int cols[100];
    
struct Line {
    int x[100];
    int dominate;

    Line() {
        for(int i = 0; i < 100; ++i) x[i] = 0;
    }

    // for sort
    bool operator <(const Line& o) const {
        for (int i = 0; i < 100; ++i) {
            if (x[i] == o.x[i]) continue;
            return x[i] < o.x[i];
        }
        return 0;
    }

    bool is_small(const Line &o) const {
        for (int i = 0; i < N; ++i) {
            if (x[i] <= o.x[i]) return false;
        }
        return true;
    }

};

Line lines[100];
bool solved;

void go(int ii, int row, int col, int x)
{
    //cout << ii << " " << row <<  " " <<col << " " << x << endl;
    if (ii == M) {
        solved = true;

        /*
        for(int i = 0; i < row; ++i) 
            cout << rows[i] << " ";
        cout << endl;

        for(int i = 0; i < col; ++i) 
            cout << cols[i] << " ";
        cout << endl;
        */

        if (x == -1) {
            if (row < N) {
                for(int i = 0; i < N; ++i) {
                    cout << lines[cols[i]].x[N-1] << " ";
                }
                cout << endl;
            }
            else {
                for(int i = 0; i < N; ++i) {
                    cout << lines[rows[i]].x[N-1] << " ";
                }
                cout << endl;
            }
            return;
        }
        else {
            if (x >= 1000) {
                x -= 1000;
                for(int i = 0; i < N; ++i) {
                    cout << lines[rows[i]].x[x] << " ";
                }
                cout << endl;
            }   
            else {
                for(int i = 0; i < N; ++i) {
                    cout << lines[cols[i]].x[x] << " ";
                }
                cout << endl;
            } 
        }
    }

    Line line = lines[ii];

    // for column
    if (col < N) {
        bool valid = true;

        if (col-1 == x-1000 || col == 0 || line.is_small(lines[cols[col-1]])) {
        }
        else {
            valid = false;
        }
        for(int i = 0; i < row; ++i) {
            if (line.x[i] == lines[rows[i]].x[col]) continue;
            if (x >= 0 && x == i) continue;
            valid = false;
        }
        if (valid) {
            cols[col] = ii;
            go(ii + 1, row, col + 1, x);
            cols[col] = 0;
        }
    }

    if (solved) return;

    // for row
    if (row < N) {
        bool valid = true;
        if (row-1 == x || row == 0 || line.is_small(lines[rows[row-1]])) {
        }
        else {
            valid = false;
        }
        for(int i = 0; i < col; ++i) {
            if (line.x[i] == lines[cols[i]].x[row]) continue;
            if (x >= 0 && x-1000 == i) continue;
            valid = false;
        }
        if (valid) {
            rows[row] = ii;
            go(ii + 1, row + 1, col, x);
            rows[row] = 0;
        }
    }

    if (solved) return;

    // for skip??
    if (x == -1) {
        if (row < N) {
            rows[row] = 0;
            go(ii, row + 1, col, row);
            if (solved) return;
        }
        if (col < N) {
            cols[col] = 0;
            go(ii, row, col + 1, 1000 + col);
        }
    }
    
}

void solve()
{
    cin >> N;
    M = 2 * N - 1;

    for(int i = 0; i < M; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> lines[i].x[j];
        }
    }
    sort(lines + 0, lines + M);

    for (int i = 0; i < M; ++i) {
        //for(int j = 0; j < N; ++j) cout << lines[i].x[j] << " ";
        //cout << endl;
        lines[i].dominate = 0;
        for(int j = 0; j < i; ++j) {
            if (lines[i].is_small(lines[j])) lines[i].dominate++;
        }
    }

    rows[0] = 0;
    solved = false;
    for(int i = 0; i < N; ++i) { rows[0] = 0; cols[0] = 0; }
    go(1, 1, 0, -1);
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
