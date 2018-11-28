#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int **createGrid(int N, int M) {
    int **grid = new int *[N];
    for (int i = 0; i < N; i++) {
        grid[i] = new int[M];
    }
    return grid;
}

void sortedInsert(int val, vector<int> & heights) {
    for (int i = 0; i < heights.size(); i++) {
        if (heights[i] == val) return;

        if (heights[i] > val) {
            heights.insert(heights.begin() + i, val);
            return;
        }
    }
    heights.push_back(val);
}

void readGrid(ifstream & in, int **grid, int N, int M, vector<int> & heights, map<int,int> & heightCounts) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            in >> grid[i][j];

            sortedInsert(grid[i][j], heights);
            if (heightCounts.count(grid[i][j]) == 0) {
                heightCounts[grid[i][j]] = 1;
            } else {
                heightCounts[grid[i][j]]++;
            }
        }
    }
}

bool confirmRowCol(int **grid, int N, int M, vector<int> & heights, map<int, int> & heightCounts, int & numbConfirmed) {
    if (heights.size() == 0) return false;

    //type = 0 for row, type = 1 for cols
    for (int type = 0; type < 2; type++) {
        int imax = (type == 0) ? N : M;
        int jmax = (type == 0) ? M : N;
        for (int i = 0; i < imax; i++) {
            bool rowConfirmed = true;
            int numbHeights = 0;
            for (int j = 0; j < jmax; j++) {
                int val = (type == 0) ? grid[i][j] : grid[j][i];

                if (val != heights[0] && val != 0) {
                    rowConfirmed = false;
                    break;
                }
                if (val == heights[0]) numbHeights++;
            }

            if (rowConfirmed && numbHeights > 0) {
                for (int j = 0; j < jmax; j++) {
                    if (type == 0 && grid[i][j] == heights[0]) {
                        grid[i][j] = 0;
                    } else if (type == 1 && grid[j][i] == heights[0]) {
                        grid[j][i] = 0;
                    }
                }
                numbConfirmed += numbHeights;
                heightCounts[heights[0]] -= numbHeights;
                
                if (heightCounts[heights[0]] == 0) {
                    heights.erase(heights.begin());
                }
                return true;
            }
        }
    }
    return false;
}

int main() {
    ifstream in;
    ofstream out;

    in.open("input");
    out.open("output");

    int numbTests;
    in >> numbTests;

    for (int numb = 1; numb <= numbTests; numb++) {
        int N, M;
        in >> N;
        in >> M;

        vector<int> heights;
        map<int, int> heightCounts;

        int **grid = createGrid(N, M);
        readGrid(in, grid, N, M, heights, heightCounts);

        int numbConfirmed = 0;
        cout << "Case #" << numb << ": ";
        while (confirmRowCol(grid, N, M, heights, heightCounts, numbConfirmed)) {
        }

        out << "Case #" << numb << ": ";
        if (numbConfirmed == N * M) {
            cout << "YES";
            out << "YES";
        } else {
            cout << "NO";
            out << "NO";
        }
        out << endl;
        cout << endl;

        for (int j = 0; j < N; j++) {
            delete grid[j];
        }
        delete grid;
    }
    

    in.close();
    out.close();
    
    return 0;
}
