#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream readFile("input.txt");
    ofstream printFile("output.txt");

    int testCasesNum; readFile >> testCasesNum;

    int m[101][1001];
    int platesIntervalsNum[101];

    for(int i = 0; i < testCasesNum; i++) {
        readFile >> platesIntervalsNum[i];

        for(int j = 0; j < platesIntervalsNum[i]; j++) {
            readFile >> m[i][j];
        }
    }

    for(int i = 0; i < testCasesNum; i++) {

        int firstCaseSum = 0;
        int secondCaseSum = 0;

        for(int j = 0; j < platesIntervalsNum[i]; j++) {
            if(j < platesIntervalsNum[i] - 1) {
                if(m[i][j] - m[i][j + 1] > 0) {
                    firstCaseSum += m[i][j] - m[i][j + 1];
                }
            }

        }

        int maxDiff = 0;

        for(int j = 0; j < platesIntervalsNum[i] - 1; j++) {
            if(m[i][j] - m[i][j + 1] > maxDiff) {
                maxDiff = m[i][j] - m[i][j + 1];
            }
        }

        for(int j = 0; j < platesIntervalsNum[i] - 1; j++) {
            if(m[i][j] > maxDiff) { secondCaseSum += maxDiff; }
            else { secondCaseSum += m[i][j]; }
        }

        //secondCaseSum -= m[i][platesIntervalsNum[i] - 1];

        printFile << "Case #" << i + 1 << ": " << firstCaseSum << " " << secondCaseSum << "\n";

    }

    return 0;
}
