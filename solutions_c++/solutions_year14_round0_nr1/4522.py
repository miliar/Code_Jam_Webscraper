#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

// rowIdx indexed from 1
void readGridRow(vector<int> &row, int rowIdx)
{
    string line;
    int num;

    for (int i = 1; i <= 4; i++) {
        line.clear();
        getline(cin, line);
        if (line.length() == 0 || isspace(line[0]))
        {
            i--;
            continue;
        }

        //cout << "Read line: " << line << endl;
            
        if (i == rowIdx)
        {
            istringstream iss(line);
            
            for (int j = 0; j < 4; j++)
            {
                iss >> num;
                if (!iss.fail())
                    row.push_back(num);
                else
                    cerr << "Input error encountered on line " << line << endl;
            }
        }
    }
}

int main(int argc, char** argv) {
    int numProbs;
    int firstRowIdx, secondRowIdx;

    cin >> numProbs;

    vector<int> firstRow, secondRow;        
    vector<int> matches;

    for (int i = 0; i < numProbs; i++) {
        cin >> firstRowIdx;
        firstRow.clear();
        readGridRow(firstRow, firstRowIdx);
        
        cin >> secondRowIdx;
        secondRow.clear();
        readGridRow(secondRow, secondRowIdx); 

        sort(firstRow.begin(), firstRow.end());
        sort(secondRow.begin(), secondRow.end());

        
        int firstColIdx = 0, secondColIdx = 0;
        matches.clear();
        while (firstColIdx < firstRow.size() && secondColIdx < secondRow.size())
        {
            if (firstRow[firstColIdx] < secondRow[secondColIdx])
            {
                firstColIdx++;
            } 
            else if (firstRow[firstColIdx] > secondRow[secondColIdx])
            {
                secondColIdx++;
            }
            else
            {
                matches.push_back(firstRow[firstColIdx]);
                firstColIdx++; secondColIdx++;
            }
        }
        
        cout << "Case #" << (i+1) << ": ";
        if (matches.size() == 1)
        {
            cout << matches[0] << endl;
        }
        else if (matches.size() > 1)
        {
            cout << "Bad magician!" << endl;
        }
        else
        {
            cout << "Volunteer cheated!" << endl;
        }
    }
}
