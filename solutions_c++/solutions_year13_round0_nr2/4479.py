#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

template<typename T>
void printBoard2D (vector< vector<T> > &board) {

    for( int i = 0; i < board.size(); ++i) {

        for(int j = 0; j < board[i].size(); ++j) {
            cout << board[i][j] << " ";
        }

        cout << endl;
    }
}

template<typename T>
void printBoard1D (vector<T> &board) {

    for( int i = 0; i < board.size(); ++i) {
        cout << board[i] << " ";
    }
    cout << endl;
}

void loadLawn(vector< vector<int> > &lawn, vector<int> &maxRow,
              vector<int> &maxCol, ifstream &ins) 
{

    for (int row = 0; row < lawn.size(); ++row) {
        for(int col = 0; col < lawn[row].size(); ++col) {

            ins >> lawn[row][col];
            if(maxRow[row] < lawn[row][col]) {
                maxRow[row] = lawn[row][col];
            }

            if(maxCol[col] < lawn[row][col]) {
                maxCol[col] = lawn[row][col];
            }

        }
    }

    string junk;
    getline(ins, junk);
}

bool ckValidLawn(vector< vector<int> > &lawn, vector<int> &maxRow,
                 vector<int> &maxCol) {

    int square = -1;

    for (int row = 0; row < lawn.size(); ++row) {

        for(int col = 0; col < lawn[row].size(); ++col) {

            square = lawn[row][col];

            if( !(square >= maxRow[row] || square >= maxCol[col]) ) {
                return false;
            }

        }
    }

    return true;

}

int main(int argc, char **argv) {

    if(argc != 2) {
        cerr << "Invalid Arguments" << endl;
        return 1;
    }

    string fileName = argv[1];

    ifstream ins;

    ins.open(fileName.c_str());

    if(!ins) {
        cerr << "Bad File Name" << endl;;
        return 1;
    }

    string junk;

    int numTests;

    ins >> numTests;
    getline(ins, junk);

    int row = 0;
    int col = 0;

    for(int i = 0; i < numTests; ++i) {

        ins >> row >> col;
        getline(ins, junk);

        vector<int> maxRow(row, -1);
        vector<int> maxCol(col, -1);
        vector< vector<int> > lawn (row, vector<int>(col, 0));

        loadLawn(lawn, maxRow, maxCol, ins);

        cout << "Case #" << i + 1 << ": ";
        if( ckValidLawn(lawn, maxRow, maxCol) ){
            cout << "YES";
        }
        else {
            cout << "NO";
        }

        cout << endl;

    }


    return 0;
}


