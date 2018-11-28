#include <iostream>
#include <sstream>

using namespace std;

int solve_one() {
    int i, j, r, N, M;
    int lawn[1000][1000], max_col[1000], max_row[1000];
    string line;
    
    for (i=0; i<500; i++)
        max_col[i] = max_row[i] = -1;
    
    getline(cin, line);
    istringstream parse(line);
    parse >> N >> M;
    
    for (i=0; i<N; i++) {
        getline(cin, line);
        istringstream parse(line);
        for (j=0; j<M; j++) {
            parse >> lawn[i][j];
        }
    }

    for (i=0; i<N; i++)
        for (j=0; j<M; j++){
            if (lawn[i][j] > max_row[i])
                max_row[i] = lawn[i][j];
            if (lawn[i][j] > max_col[j])
                max_col[j] = lawn[i][j];
        }
    
    for (i=0; i<N; i++)
        for (j=0; j<M; j++) {
            if ((lawn[i][j] < max_row[i]) && (lawn[i][j] < max_col[j]))
                return 0;
        }
    
    return 1;
}

int main() {
    
    int r, t, testcases;
    string line;
    
    getline(cin, line);
    istringstream parse(line);
    parse >> testcases;
    
    for (t=1; t<= testcases; t++) {
        r = solve_one();
        if (r == 1)
            cout << "Case #" << t << ": YES\n";
        else
            cout << "Case #" << t << ": NO\n";
    }
}




