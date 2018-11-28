#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

bool checkPattern(vector<vector<size_t> > & pattern)
{
    for(size_t i = 0; i != pattern.size(); ++i)
    {
        for(size_t j = 0; j != pattern[i].size(); ++j)
        {
            size_t curCellHeight = pattern[i][j];
            bool passByRow(true);
            for(size_t k = 0; k != pattern[i].size(); ++k)
            {
                if(pattern[i][k] > curCellHeight)
                {
                    passByRow = false;
                    break;
                }
            }
            if(passByRow)
            {
                continue;
            }
            else
            {
                for(size_t k = 0; k != pattern.size(); ++k)
                {
                    if(pattern[k][j] > curCellHeight)
                    {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main(int argc, char* args[])
{

    size_t T;
    cin >> T;

    for(size_t t = 0; t != T; ++t)
    {
        size_t N, M;
        cin >> N >> M;
        vector<vector<size_t> > pattern(N);
        for(size_t i = 0; i != N; ++i)
        {   
            pattern[i] = vector<size_t>(M);
            for(size_t j = 0; j != M; ++j)
            {
                //size_t tmp;
                //cin >> tmp;
                //cout << "read" << tmp << endl;
                //pattern[i][j] = tmp;
                cin >> pattern[i][j];
            }
        }

        // for(size_t i = 0; i != pattern.size(); ++i)
        // {

        //     for(size_t j = 0; j != pattern[i].size(); ++j)
        //     {
        //         cout << pattern[i][j] << "   ";
        //     }
        //     cout << endl;
        // }
        if(checkPattern(pattern))
        {
            cout << "Case #" << t+1 << ": YES" << endl;
        }
        else
        {
            cout << "Case #" << t+1 << ": NO" << endl;
        }
    }



    return 0;
}