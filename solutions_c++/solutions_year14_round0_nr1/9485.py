#include <iostream>
using namespace std;

#define rowSize 4
#define colSize 4

main()
{
    ios::sync_with_stdio(false);
    int caseNum, firstAns, secondAns;
    int firstArrangement[rowSize][colSize], secondArrangement[rowSize][colSize];

    bool found, multiFound;
    int number;
    int caseCounter = 1;

    cin >> caseNum;
    while(caseNum--) {
        cin >> firstAns;
        for (int row = 0; row < rowSize; row++)
            for (int col = 0; col < colSize; col++)
                cin >> firstArrangement[row][col];

        cin >> secondAns;
        for (int row = 0; row < rowSize; row++)
            for (int col = 0; col < colSize; col++)
                cin >> secondArrangement[row][col];

        found = false;
        multiFound = false;
        for (int col1 = 0; col1 < colSize; col1++)
            for (int col2 = 0; col2 < colSize; col2++)
                if (firstArrangement[firstAns-1][col1] == secondArrangement[secondAns-1][col2])
                    if (!found) {
                        number = firstArrangement[firstAns-1][col1];
                        found = true;
                    } else if (!multiFound)
                        multiFound = true;

        cout << "Case #" << caseCounter++ << ": ";
        if (multiFound)
            cout << "Bad magician!" << endl;
        else if (found)
            cout << number << endl;
        else
            cout << "Volunteer cheated!" << endl;
    }
}
