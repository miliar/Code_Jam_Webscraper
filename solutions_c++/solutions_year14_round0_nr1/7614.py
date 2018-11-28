#include <iostream>
#include <fstream>
#include <vector>

#define CHEATED 0
#define DUMB -1
using namespace std;

int main()
{
    ifstream fin ("solve.in");
    int N;
    fin >> N;

    vector<int> results;

    for (int i = 0; i < N; i++)
    {
        int row;
        fin >> row;
        vector<vector<int> > cards1;
        for(int j = 0; j < 4; j++)
        {
            vector<int> row;
            cards1.push_back(row);
            for (int k = 0; k < 4; k++)
            {
                int card;
                fin >> card;
                cards1[j].push_back(card);
            }
        }
        vector<int> firstRow = cards1[row - 1];
        fin >> row;

        vector<vector<int> > cards2;
        for(int j = 0; j < 4; j++)
        {
            vector<int> row;
            cards2.push_back(row);
            for (int k = 0; k < 4; k++)
            {
                int card;
                fin >> card;
                cards2[j].push_back(card);
            }
        }
        vector<int> secondRow = cards2[row - 1];
        
        vector<int> intersection;
        for(int j = 0; j < 4; j++)
        {
            int card = secondRow[j];
            for(int k = 0; k < 4; k++)
            {
                if(firstRow[k] == card)
                {
                    intersection.push_back(card);
                    break;                    
                }
            }
        }
        if(intersection.size() == 0)
            results.push_back(CHEATED);
        else if(intersection.size() == 1)
            results.push_back(intersection[0]);
        else
            results.push_back(DUMB);

    }   
    fin.close();
 
    ofstream fout ("solve.out");
    for(int i = 0; i < results.size(); i++)
    {
        if(results[i] != DUMB && results[i] != CHEATED)
            fout << "case #" << (i + 1) << ": " << results[i] << "\n";
        if(results[i] == DUMB)
            fout << "case #" << (i + 1) << ": " << "Bad magician!\n";
        if(results[i] == CHEATED)
            fout << "case #" << (i + 1) << ": " << "Volunteer cheated!\n";
            
    }
    return 0;
}
