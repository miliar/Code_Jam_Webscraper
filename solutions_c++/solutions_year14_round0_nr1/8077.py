#include <iostream>
#include <algorithm>
#include <string>
#include <list>
#include <vector>
#include <fstream>
using namespace std;
void printVec(vector<int> vec);
bool isIn(int n, vector<int> row);
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in.txt");
    fout.open("output.txt");

    int numCases = 0;
    int row1;
    int row2;
    int num;
    int numMatches = 0;
    vector<int> row (4, 0);
    vector<int> nextRow (4, 0);
    fin >> numCases;
    string s;
    int caseNum = 1;
    while(numCases > 0)
    {
        fin >> row1;

        for(int i = 0; i < 4*(row1 - 1); i++)
        {
            fin >> num;
        }
        for(int i = 0; i < 4; i++)
        {
            fin >> num;
            row[i] = num;
        }
        for(int i = 0; i < 4*(4 - row1); i++)
        {
            fin >> num;
        }

        //**** next row
        fin >> row2;
        for(int i = 0; i < 4*(row2 - 1); i++)
        {
            fin >> num;
        }
        for(int i = 0; i < 4; i++)
        {
            fin >> num;
            nextRow[i] = num;
        }
        for(int i = 0; i < 4*(4 - row2); i++)
        {
            fin >> num;
        }

        //*** checking cases
        for(int i = 0; i < 4; i++)
        {
            if(isIn(row[i], nextRow))
            {
                numMatches++;
                num = row[i];
            }
        }
        fout << "Case #" << caseNum << ": ";
        if(numMatches == 0)
        {
            fout << "Volunteer cheated!" << endl;
        }
        if(numMatches == 1)
        {
            fout << num << endl;
        }
        if(numMatches > 1)
        {
            fout << "Bad magician!" << endl;
        }

        numMatches = 0;
        numCases--;
        caseNum++;
    }
    return 0;
}

void printVec(vector<int> vec)
{
    for(int i = 0; i < vec.size(); i++)
    {
        cout << vec[i] << " ";
    }
    cout << endl;
    return;
}

bool isIn(int n, vector<int> row)
{
    for(int i = 0; i < row.size(); i++)
    {
        if(n == row[i])
        {
            return true;
        }
    }
    return false;
}
