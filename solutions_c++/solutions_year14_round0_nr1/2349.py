#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("A.in");
    ofstream fout("A.out");
    int T, row, card;
    fin >> T;
    for (int testnum = 1; testnum <= T; testnum++)
    {
        vector<int> grid[2], intersect;
        for (int i = 0; i < 2; i++)
        {
            fin >> row;
            for (int j = 1; j <= 4*(row-1); j++)
                fin >> card;
            for (int j = 0; j < 4; j++)
            {
                fin >> card;
                grid[i].push_back(card);
            }
            for (int j = 1; j <= 4*(4-row); j++)
                fin >> card;
            sort(grid[i].begin(), grid[i].end());
        }
        set_intersection(grid[0].begin(), grid[0].end(), grid[1].begin(), grid[1].end(), back_inserter(intersect));
        fout << "Case #" << testnum << ": ";
        if (intersect.size() == 0)
            fout << "Volunteer cheated!" << endl;
        else if (intersect.size() == 1)
            fout << intersect[0] << endl;
        else
            fout << "Bad magician!" << endl;
    }
}