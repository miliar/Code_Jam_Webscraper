#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
    int n;
    fin >> n;
    
    for (int i = 0; i < n; i++)
    {
        int row_1 = 0;
        int row_2 = 0;
        vector<vector<int> > board_1;
        vector<vector<int> > board_2;
        vector<int> results;
        fin >> row_1;
        for (int j = 0; j < 4; j++)
        {
            vector<int> row;
            int buffer;
            for (int k = 0; k < 4; k++)
            {
                fin >> buffer;
                row.push_back(buffer);
            }
            board_1.push_back(row);
        }
        fin >> row_2;
        for (int j = 0; j < 4; j++)
        {
            vector<int> row;
            int buffer;
            for (int k = 0; k < 4; k++)
            {
                fin >> buffer;
                row.push_back(buffer);
            }
            board_2.push_back(row);
        }
        for (int j = 0; j < 4; j++)
        {
            //cout << board_1[row_1][j] << ", " << board_2[row_2][j] << '\n';
            for (int k = 0; k < 4; k++)
            {
                if (board_1[row_1 - 1][j] == board_2[row_2 - 1][k])
                {
                    if (find(results.begin(), results.end(), board_1[row_1 - 1][j]) == results.end())
                        results.push_back(board_1[row_1 - 1][j]);
                }
            }
        }
        //cout << row_1 << ", " << row_2 << '\n';
        fout << "Case" << " #" << i + 1 << ": ";
        //cout << "Case" << " #" << i + 1 << ": ";
        for (int j = 0; j < results.size(); j++)
        {
            //cout << results[j] << ", ";
        }
        if (results.size() > 1)
        {
            fout << "Bad magician!\n";
            //cout << "Bad magician!\n";
        }
        else if (results.size() == 0)
        {
            fout << "Volunteer cheated!\n";
            //cout << "Volunteer cheated!\n";
        }
        else if (results.size() == 1)
        {
            fout << results[0] << '\n';
            //cout << results[0] << '\n';
        }
    }
}
