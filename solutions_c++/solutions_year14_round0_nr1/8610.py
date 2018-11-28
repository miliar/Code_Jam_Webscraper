#include <iostream>
#include <fstream>
using namespace std;

const int ARR_SIZE = 4;

int **ReadBuf(ifstream &stream)
{
    int **buf;
    buf = new int *[ARR_SIZE];
    for(int i = 0; i < ARR_SIZE; i++)
    {
        buf[i] = new int[ARR_SIZE];
        for(int j = 0; j < ARR_SIZE; j++)
        {
            stream >> buf[i][j];
        }
    }

    return buf;
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("testOut.txt");

    int T;
    fin >> T;
    for(int testCount = 1; testCount <= T; testCount++)
    {
        int first_answer;
        fin >> first_answer;
        int **first_matrix = ReadBuf(fin);
        int second_answer;
        fin >> second_answer;
        int **second_matrix = ReadBuf(fin);

        int count = 0;
        int output = 0;
        for(int i = 0; i < ARR_SIZE; i++)
        {
            for(int j = 0; j < ARR_SIZE; j++)
            {
                if(first_matrix[first_answer-1][i] == second_matrix[second_answer-1][j])
                {
                    count++;
                    output = first_matrix[first_answer-1][i];
                }
            }
        }

        fout << "Case #" << testCount << ": ";
        if(count == 0)
        {
            fout << "Volunteer cheated!";
        }
        if(count == 1)
        {
            fout << output;
        }
        if(count > 1)
        {
            fout << "Bad magician!";
        }

        fout << endl;

        // free
        for(int i = 0; i < ARR_SIZE; i++)
        {
            delete [] first_matrix[i];
            delete [] second_matrix[i];
        }
        delete [] first_matrix;
        delete [] second_matrix;
    }
    return 0;
}
