#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <vector>
// #include <map>
// #include <algorithm>
#include <set>

using namespace std;
typedef vector<int> IntVec;
typedef set<int> IntSet;
typedef vector<IntVec> Lawn;
struct Coord {
    Coord(int x, int y) {
        this->x = x;
        this->y = y;
    }
    Coord(const Coord &other) {
        this->x = other.x;
        this->y = other.y;
    }
    bool operator< (const Coord& others) const { 
        if ( (x + 101 * y)  < (others.x + 101 * others.y)) {
            return true;
        }
        return false;
        /* do actual comparison */ 
    }

    int x;
    int y;
};

typedef set<Coord> Coords;
// typedef map<int, Coord> SearchTable;

void printLawn(ostream &out, const Lawn &lawn) {
    int N = lawn.size();
    int M = lawn[0].size();
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            out << lawn[i][j];
        }
        out << endl;
    }
}

void convertToIntVec(string line, IntVec &res) {;
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atol(next));
        next = strtok(NULL, " ");
    }
    free(list);
}



bool checkFeasibility(const Lawn &lawn) {
    // Lawn mttc = lawn;
    int N = lawn.size();
    int M = lawn[0].size();
    Coords okayPts;

    for (int i = 0; i < N; ++i ) {
        // find max element in this row
        int maxEle = -1;
        for (int j = 0; j < M; ++j) {
            if (lawn[i][j] > maxEle) {
                maxEle = lawn[i][j];
            }
        }

        for (int j = 0; j < M; ++j) {
            if (lawn[i][j] == maxEle) {
                // okayRows.insert()
                Coord pt2(i, j);
                okayPts.insert(pt2);
            }
        }

    }

    for (int j = 0; j < M; ++j) {
        // max element in this column.
        int maxEle = -1;
        for (int i = 0; i < N; ++i) {
            if (lawn[i][j] > maxEle) {
                maxEle = lawn[i][j];
            }
        }

        for (int i = 0; i < N; ++i) {
            if (lawn[i][j] == maxEle) {
                okayPts.insert(Coord(i, j));
            }
        }

    }

    if (okayPts.size() == N * M) {
        return true;
    }
    return false;

}


int main(int argc, char *argv[]) {
    // ifstream inFile("tiny.in");
    // ifstream inFile("B-small-attempt3.in");
    ifstream inFile("B-large.in");
    // ofstream outFile("B-small-attempt0.out");
    // ofstream outFile("B-small-attempt3.out");
    ofstream outFile("B-large.out");
    // ifstream inFile("A-small-attempt0.in");
    // ofstream outFile("A-small-attempt0.out");
    // ifstream inFile("A-large.in");
    // ofstream outFile("A-large.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());

    for (int i = 0; i < T; ++i) {
        Lawn lawn;

        IntVec lawnSize;
        getline(in, line);
        convertToIntVec(line, lawnSize);
        int N = lawnSize[0];
        int M = lawnSize[1];
        // cout << "N: " << lawnSize[0] << " M: " << lawnSize[1] << endl;
        
        for (int j = 0; j < N; ++j) {
            getline(in, line);
            IntVec row;
            convertToIntVec(line, row);
            lawn.push_back(row);
            // getline(in, line);
        }
        // printLawn(out, lawn);
        string msg = (checkFeasibility(lawn) ?  "YES" : "NO");
        out << "Case #" << i+1 << ": " << msg << endl;
        // out << "Case #" << i+1 << ": " << checkStatus(bd) << endl;
        //
    }
    return 0;
}
