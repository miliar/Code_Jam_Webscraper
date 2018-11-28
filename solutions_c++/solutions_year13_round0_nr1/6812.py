#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    int N = 0;
    input >> N;
    for(int i = 1; i <= N; ++i)
    {
        short win = -1;
        bool notfinished = false;
        short t[4][4];
        for(int j = 0; j < 4; ++j)
        {
            for(int k = 0; k < 4; ++k)
            {
                char e;
                input >> e;
                switch(e)
                {
                    case 'X': t[j][k] = 1;
                        break;
                    case 'O': t[j][k] = 10;
                        break;
                    case '.': t[j][k] = -10;
                        break;
                    case 'T': t[j][k] = 5;
                        break;
                }
            }
        }
        int diag1 = 0;
        int diag2 = 0;
        for(int j = 0; j < 4; ++j)
        {
            int rowsum = 0;
            int colsum = 0;
            for(int k = 0; k < 4; ++k)
            {
                rowsum += t[j][k];
                colsum += t[k][j];
                if(t[j][k] == -10)
                    notfinished = true;
            }
            if(rowsum == 4 || rowsum == 8 || colsum == 4 || colsum == 8)
            {
                win = 1;
                break;
            }
            else if(rowsum == 35 || rowsum == 40 || colsum == 35 || colsum == 40)
            {
                win = 2;
                break;
            }
            diag1 += t[j][j];
            diag2 += t[j][3-j];
        }
        if(win == -1)
        {
            if(diag1 == 4 || diag1 == 8 || diag2 == 4 || diag2 == 8)
            {
                win = 1;
            }
            else if(diag1 == 35 || diag1 == 40 || diag2 == 35 || diag2 == 40)
            {
                win = 2;
            }
        }
        if(win == 1)
        {
            output << "Case #" << i << ": X won" << endl;
        }
        else if(win == 2)
        {
            output << "Case #" << i << ": O won" << endl;
        }
        else if(notfinished)
        {
            output << "Case #" << i << ": Game has not completed" << endl;
        }
        else
        {
            output << "Case #" << i << ": Draw" << endl;
        }
    }
    input.close();
    output.close();
    return 0;
}
