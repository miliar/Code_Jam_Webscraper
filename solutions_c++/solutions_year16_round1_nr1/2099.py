//
//  main.cpp / Rank and File
//  CodeJam2016
//
//  문제: NxN 크기의 배열이 나오는데,
//      거기에서 가능한 배열의 가로 세로 숫자들은 대충 2N 개가 나온다. 가로 N개, 세로 N개.
//      그리고 그 중에 1개 배열이 날아감. 그게 뭘까?
//      최대 가로 세로 50, 최대 키 2500, 테스트 케이스 50개.
//
//      정렬을 하되, 왼쪽 위에 1이 떨어지도록 정렬하고, 그 뒤에 채워나가는 식으로 때리면 되지 않을까?

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void runQuestion(int number)
{

    // input
    char inputString[1001];
    cin >> inputString;

    // setting
    char resultString[1001];
    char resultCache[1001];

    // find result

    resultString[0] = inputString[0];
    resultString[1] = '\0';

    for ( int i = 1 ; i < strlen(inputString) ; i++ ) {
        // cout << "input" << inputString[i] << " vs " << resultString[0] << endl;
        if ( inputString[i] >= resultString[0] ) {
            sprintf(resultCache, "%c%s", inputString[i], resultString);
        }
        else {
            sprintf(resultCache, "%s%c", resultString, inputString[i]);
        }
        // cout << "result:" << resultCache << endl;
        strcpy(resultString, resultCache);
    }

    // for ( int i = 0 ; i < 2500 ; i++ ) {
    //     if ( heights[i] != 0 ) {
    //         cout << "RESULT::" << i << "::" << heights[i] << endl;
    //     }
    // }

    // output
    cout << "Case #" << number << ": " << resultString;
    cout << endl;
}

int main(int argc, const char * argv[]) {

    int howManyTimes;

    scanf("%d", &howManyTimes);

    for ( int i = 0 ; i < howManyTimes ; i++ ) {
        runQuestion(i+1);
    }

    return 0;
}

