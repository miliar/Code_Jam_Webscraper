#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int cases, first, second, temp, count=0;
    ifstream fin ("first.in");
    ofstream fout ("output.txt");
    fin>>cases;
    for (int i=0; i<cases; i++)
    {
        vector<vector<int> > arrangeFirst;
        vector<vector<int> > arrangeSecond;
        fin>>first;
        for (int j=0; j<4; j++)
        {
            vector<int> newRow;
            for (int k=0; k<4; k++)
            {
                fin>>temp;
                newRow.push_back(temp);
            }
            arrangeFirst.push_back(newRow);
        }
        fin>>second;
        for (int j=0; j<4; j++)
        {
            vector<int> newRow;
            for (int k=0; k<4; k++)
            {
                fin>>temp;
                newRow.push_back(temp);
            }
            arrangeSecond.push_back(newRow);
        }
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                if (arrangeFirst[first-1][j] == arrangeSecond[second-1][k])
                {
                                             temp = arrangeFirst[first-1][j];
                                             count++;
                                             break;
                }
            }
        }
        if (count==1)
        fout<<"Case #"<<i+1<<": "<<temp<<endl;
        else if (count>1)
        fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        else if (count==0)
        fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        count=0;
    }
    return 0;
}
