#include <iostream>
#include<cassert>
using namespace std;

#define MAX_DEPTH   (4)
 
int **a;
int **dir;

#define H (1)
#define V (2)

void init_dir(int rowMax, int colMax)
{
    for (int i = 0; i < rowMax; i++) {
        for (int j = 0; j < colMax; j++) {
            dir[i][j] = 3;
        }
    }
}

bool hCheck(int row, int col, int colMAX)
{
    int &value = dir[row][col];
    for (int c = 0; c < colMAX; c++) {
        // dont check same col 
        if (c == col)
            continue;

        // check value array
        if (a[row][c] > a[row][col]) {
            //modify dir array
            value = value & V;
            if (!value)
                return false;
        } else if (a[row][c] < a[row][col]) {
            dir[row][c] &= V;
            if (!dir[row][c])
                return false;
        }
    }

    return true;
}

bool vCheck(int row, int col, int rowMAX)
{
    int &value = dir[row][col];
    for (int r = 0; r < rowMAX; r++) {
        // dont check same col 
        if (r == row)
            continue;

        // check value array
        if (a[r][col] > a[row][col]) {
            //modify dir array
            value = value & H;
            if (!value)
                return false;
        } else if (a[r][col] < a[row][col]) {
            dir[r][col] &= H;
            if (!dir[row][col])
                return false;
        }
    }
    return true;
}


void runCase(int tcase, int rowMax, int colMax) 
{
    // creating and init direction array
    dir = new int*[rowMax];
    for (int i = 0; i < rowMax; ++i) {
      dir[i] = new int[colMax];
    }
    init_dir(rowMax, colMax);

    cout<<"Case #"<<tcase<<": ";
    for (int i=0; i < rowMax; i++) {
        for(int j=0; j < colMax; j++) {
            if (!(hCheck(i, j, colMax) && vCheck(i, j, rowMax))) {
                cout<<"NO"<<endl;
                goto on_error;
            }
        }
    }

    cout<<"YES"<<endl;

on_error:
    // destroying direction array
    for (int i = 0; i < rowMax; ++i) {
      delete [] dir[i];
    }

    delete [] dir;
}


int main(int argc, char** argv)
{
    int ntcases = 1;
    int b[4][4] = {
        /*{'X','X','X','T'},
        {'.','.','.','.'},
        {'O','O','.','.'},
        {'.','.','.','.'}*/
        {'X','O','X','T'},
        {'X','X','O','O'},
        {'O','X','O','X'},
        {'X','X','O','O'}
    };

    cin>>ntcases;
    for (int tcase = 0; tcase < ntcases; tcase++) {
        // fill array first for case,
        int N, M;
        cin>>N;
        cin>>M;

        // creating and init value array
        a = new int*[N];
        for (int i = 0; i < N; ++i) {
          a[i] = new int[M];
        }

        for (int i=0; i <N; i++) {
            for(int j=0; j<M; j++) {
                int temp;
                cin>>temp;
                a[i][j] = temp;
                //a[i][j] = b[i][j];
            }
        }
        runCase(1 + tcase, N, M);

        // creating and init value array
        for (int i = 0; i < N; ++i) {
          delete [] a[i];
        }
        delete [] a;
    }


    return 0;
}