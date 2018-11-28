#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

ifstream *input;
string getLine() {
    string line;
    if (input)
        getline(*input, line);
    else
        getline(std::cin, line);
    return line;
}

int main (int argc, char * argv[]) {
    int T;

    string s, line;
    if (argc > 1) {
        input = new ifstream(argv[1], std::ios_base::in);
        if (!input->good()) {
            return -1;
        }
    }

    line = getLine();
    if (line.length() == 0 || line == "\n") {
        return 0;
    }
    {
        stringstream ss(line);
        ss >> T;
        if (T == 0) {
            return 0;
        }
    }
    
    bool *result = new bool[T];
    for (int i = 0; i < T; i++) {
        line = getLine();
        int N, M, max = 0, min = 100;
        stringstream ss(line);
        {
            getline(ss, s, ' ');
            stringstream ss_(s);
            ss_ >> N;
        }
        {
            getline(ss, s);
            stringstream ss_(s);
            ss_ >> M;
        }
        std::vector<int> rows_max(N, 0);
        std::vector<int> cols_max(M, 0);
        int **g = new int*[N];
        for (int n = 0; n < N; n++) {
            g[n] = new int[M];
            line = getLine();
            stringstream ss(line);
            for (int m = 0; m < M; m++) {
                if (m == M - 1)
                    getline(ss, s);
                else
                    getline(ss, s, ' ');
                stringstream ss_(s);
                ss_ >> g[n][m];
                if (g[n][m] > max)
                    max = g[n][m];
                if (g[n][m] < min)
                    min = g[n][m];
                if (g[n][m] > rows_max[n])
                    rows_max[n] = g[n][m];
                if (g[n][m] > cols_max[m])
                    cols_max[m] = g[n][m];
            }
        }

        bool ok = true;
        for (int j = max; j >= min; j--) {
            std::vector<int> row_index;
            std::vector<int> col_index;
            for (int n = 0; n < N; n++) {
                for (int m = 0; m < M; m++) {
                    if (g[n][m] == j) {
                        row_index.push_back(n);
                        col_index.push_back(m);
                    }
                }
            }
            assert(row_index.size() == col_index.size());
            for (int n = 0; n < row_index.size(); n++) {
                if (j < rows_max[row_index[n]] && j < cols_max[col_index[n]]) {
                    ok = false;
                    break;                
                }
                if (!ok)
                    break;                
            }
            if (!ok)
                break;                
        }
        result[i] = ok;

        //free memory
        for (int n = 0; n < N; n++) {
            delete [] g[n];
        }
        delete [] g;
        g = NULL;
    }

    if (input) {
        input->close();
        delete input;
    }
    for (int i = 0; i < T; i++) {
        if (result[i])
            cout << "Case #" << i + 1 << ": YES" << endl;
        else
            cout << "Case #" << i + 1 << ": NO" << endl;
        /*
        if (i != T - 1) {
            cout << endl;
        }
        */
    }
    delete [] result;
}
