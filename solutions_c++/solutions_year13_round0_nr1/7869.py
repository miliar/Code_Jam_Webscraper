#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cstring>

#define DIM 4
#define N 2
#define X 1
#define O 0

using namespace std;

int testCases;

int rowWon(char mat[DIM][DIM])
{
    int consecutiveX;
    int consecutiveO;

    for (int i=0; i<DIM; i++)
    {
        consecutiveX = 0;
        consecutiveO = 0;
        for (int j=0; j<DIM; j++)
        {
            if (mat[i][j] == 'X' || mat[i][j] == 'T') consecutiveX++;
            else consecutiveX = 0;

            if (mat[i][j] == 'O' || mat[i][j] == 'T') consecutiveO++;
            else consecutiveO = 0;

            if (consecutiveX == DIM) return X;
            if (consecutiveO == DIM) return O;
        }
    }
    return N;
}

int colWon(char mat[DIM][DIM])
{
    int consecutiveX;
    int consecutiveO;

    for (int i=0; i<DIM; i++)
    {
        consecutiveX = 0;
        consecutiveO = 0;
        for (int j=0; j<DIM; j++)
        {
            if (mat[j][i] == 'X' || mat[j][i] == 'T') consecutiveX++;
            else consecutiveX = 0;

            if (mat[j][i] == 'O' || mat[j][i] == 'T') consecutiveO++;
            else consecutiveO = 0;

            if (consecutiveX == DIM) return X;
            if (consecutiveO == DIM) return O;
        }
    }
    return N;
}

int ldiagWon(char mat[DIM][DIM])
{
    int consecutiveX;
    int consecutiveO;
    int z;

    for (int slice = 0; slice < 2 * DIM - 1; ++slice)
    {
    	consecutiveX = 0;
        consecutiveO = 0;

        z = slice < DIM ? 0 : slice - DIM + 1;
    	for (int j = z; j <= slice - z; ++j)
        {
    		if (mat[j][slice-j] == 'X' || mat[j][slice-j] == 'T') consecutiveX++;
            else consecutiveX = 0;

            if (mat[j][slice-j] == 'O' || mat[j][slice-j] == 'T') consecutiveO++;
            else consecutiveO = 0;

            if (consecutiveX == DIM) return X;
            if (consecutiveO == DIM) return O;
    	}
    }
    return N;
}

int rdiagWon(char mat[DIM][DIM])
{
    int consecutiveX;
    int consecutiveO;
    int z;

    for (int slice = 0; slice < 2 * DIM - 1; ++slice)
    {
    	consecutiveX = 0;
        consecutiveO = 0;

        z = slice < DIM ? 0 : slice - DIM + 1;
    	for (int j = z; j <= slice - z; ++j)
        {
    		if (mat[j][(DIM-1)-(slice-j)] == 'X' || mat[j][(DIM-1)-(slice-j)] == 'T') consecutiveX++;
            else consecutiveX = 0;

            if (mat[j][(DIM-1)-(slice-j)] == 'O' || mat[j][(DIM-1)-(slice-j)] == 'T') consecutiveO++;
            else consecutiveO = 0;

            if (consecutiveX == DIM) return X;
            if (consecutiveO == DIM) return O;
    	}
    }
    return N;
}

int emptyCount(char mat[DIM][DIM])
{
    int count = 0;
    for (int i=0; i<DIM; i++)
    {
        for (int j=0; j<DIM; j++)
        {
            if (mat[i][j] == '.') count++;
        }
    }
    return count;
}

int main(void)
{
    int res;
    string fline;
    ifstream infile ("A-large.in");

    ofstream myfile;
    myfile.open ("file.out");

    if (infile.is_open()) getline(infile,fline);
    testCases = atoi(fline.c_str());

    char gridMatrix[DIM][DIM];

    for (int i=0; i<testCases; i++)
    {
        // Load into matrix
        for (int j=0; j<DIM; j++)
        {
            getline(infile,fline);
            for (int k=0; k<DIM; k++) gridMatrix[j][k] = fline.c_str()[k];
        }
        getline(infile,fline);

        // Check conditions
        myfile << "Case #" << i+1 << ": ";
        res = rowWon(gridMatrix);
        if (res == X) myfile << "X won" << endl;
        else if (res == O) myfile << "O won" << endl;
        else
        {
            res = colWon(gridMatrix);
            if (res == X) myfile << "X won" << endl;
            else if (res == O) myfile << "O won" << endl;
            else
            {
                res = ldiagWon(gridMatrix);
                if (res == X) myfile << "X won" << endl;
                else if (res == O) myfile << "O won" << endl;
                else
                {
                    res = rdiagWon(gridMatrix);
                    if (res == X) myfile << "X won" << endl;
                    else if (res == O) myfile << "O won" << endl;
                    else
                    {
                        if (emptyCount(gridMatrix) == 0) myfile << "Draw" << endl;
                        else myfile << "Game has not completed" << endl;
                    }
                }
            }
        }
    }

    infile.close();
    myfile.close();
    return EXIT_SUCCESS;
}
