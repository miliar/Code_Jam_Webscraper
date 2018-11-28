#include <iostream>
#include <list>
#include <vector>
#include <algorithm>


std::vector<int> pointsXCol(4),
    pointsXLin(4),
    pointsOCol(4),
    pointsOLin(4);
    
int pointsXDiagLTR,
    pointsXDiagRTL,
    pointsODiagLTR,
    pointsODiagRTL;
bool finished = true;


void runTestCase();
void parseLine(unsigned int lineNumber, std::string line);
void printState();

int main() {
    int numberOfTestCases = 0, caseTotal = 0;
    
    std::cin >> numberOfTestCases;
    caseTotal = numberOfTestCases;
    for ( ; numberOfTestCases > 0; numberOfTestCases-- ) {
        std::cout << "Case #" << (caseTotal-numberOfTestCases)+1 << ": ";
        runTestCase();
    }
    
    return 0;
}

void runTestCase() {
    std::string line;
    std::fill(pointsXLin.begin(), pointsXLin.end(), 0);
    std::fill(pointsXCol.begin(), pointsXCol.end(), 0);
    std::fill(pointsOLin.begin(), pointsOLin.end(), 0);
    std::fill(pointsOCol.begin(), pointsOCol.end(), 0);
    pointsXDiagLTR = 0;
    pointsXDiagRTL = 0;
    pointsODiagLTR = 0;
    pointsODiagRTL = 0,
    finished = true;

    for ( unsigned int numberOfInputLines = 0; numberOfInputLines < 4; numberOfInputLines++ ) {
        std::cin >> line;
        parseLine(numberOfInputLines, line);
    }
    
    printState();
}

void parseLine(unsigned int lineNumber, std::string line) {
    for(std::string::size_type i = 0; i < line.size(); ++i) {
        if ( line[i] == 'X' ) {
            pointsXLin[lineNumber] += 1;
            pointsXCol[i] += 1;
            
            if (lineNumber == i) pointsXDiagLTR += 1;
            if (lineNumber + i == 3) pointsXDiagRTL += 1;
        }
        if ( line[i] == 'O' ) {
            pointsOLin[lineNumber] += 1;
            pointsOCol[i] += 1;
            
            if (lineNumber == i) pointsODiagLTR += 1;
            if (lineNumber + i == 3) pointsODiagRTL += 1;
        }
        if ( line[i] == 'T' ) {
            pointsXLin[lineNumber] += 1;
            pointsXCol[i] += 1;
            pointsOLin[lineNumber] += 1;
            pointsOCol[i] += 1;
            
            if (lineNumber == i) {
                pointsXDiagLTR += 1;
                pointsODiagLTR += 1;
            }
            if (lineNumber + i == 3) {
                pointsXDiagRTL += 1;
                pointsODiagRTL += 1;
            }
        }
        if ( line[i] == '.' ) {
            finished = false;
        }
    }
}

void printState() {
    bool winX = false, winO = false;
    
    for (int i = 0; i < 4; i++) {
        if ( pointsXLin[i] == 4 || pointsXCol[i] == 4 || pointsXDiagLTR == 4 || pointsXDiagRTL == 4 )
            winX = true;
        if ( pointsOLin[i] == 4 || pointsOCol[i] == 4 || pointsODiagLTR == 4 || pointsODiagRTL == 4 )
            winO = true;
    }
    
    if ( winX ) std::cout << "X won" << std::endl;
    else if ( winO ) std::cout << "O won" << std::endl;
    else if ( finished ) std::cout << "Draw" << std::endl;
    else std::cout << "Game has not completed" << std::endl;
}

