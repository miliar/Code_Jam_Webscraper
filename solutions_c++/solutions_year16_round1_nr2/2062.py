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
    int t_size;
    cin >> t_size;
/*
    int inputHeight[100][50][2];    // [행][열][사용됨/안됨]
    for ( int i = 0 ; i < t_size ; i++ ) {
        for ( int j = 0 ; j < t_size ; j++ ) {
            cin >> inputHeight[i][j][0];
        }
    }

    // setting
    int resultMatrix[51][51];   // [0,x], [y,0] 은 사용되었음을 의미하고, 1~50까지가 입력값.

    // pre-processing
    resultMatrix[0][0] = -1;

    for ( int i = 1 ; i < 51 ; i++ ) {
        resultMatrix[0][i] = 0; // 기본값. 사용되지 않았음
        resultMatrix[i][0] = 0;

        if ( i > t_size ) {
            resultMatrix[0][i] = -1;    // 기본값. 이 row/col은 사용될 일이 없음.
            resultMatrix[i][0] = -1;
        }
    }

    // NOPE!!
    // calculation
    // 1. Find Minimum left top
    // 2. Find Maximum right bottom
    // 3. Sort
    // 4. Insert every row/column.
    // NOPE!!

    // result search
    int result[50];
    int result[0] = -1;

    for ( int i = 1 ; i < 51 ; i ++ ) {
        if ( resultMatrix[0][i] == -1 || resultMatrix[i][0] == -1 )
            break;

        if ( resultMatrix[0][i] == 0 ) {
            for ( j = 0 ; j < 50 ; j ++ ) {
                result[j] = resultMatrix[j+1][i];
            }
        }
        else if ( resultMatrix[i][0] == 0 ) {
            for ( j = 0 ; j < 50 ; j ++ ) {
                result[j] = resultMatrix[i][j+1];
            }
        }
    }
    if ( result[0] == -1 )
        cout << "ERROR: No Answer";

*/
    // ...잠깐 이거 설마 숫자 무조건 두 번씩 나오는...
    // ...계산 수정.
    //
    // Every Number should show twice, and any number shows one time, it's result.

    int inputHeight[100][50];    // [행][열][사용됨/안됨]
    for ( int i = 0 ; i < t_size*2-1 ; i++ ) {
        for ( int j = 0 ; j < t_size ; j++ ) {
            cin >> inputHeight[i][j];
        }
    }

    // setting
    int heights[2500];
    for ( int i = 0 ; i < 2500 ; i++ ) {
        heights[i] = 0;
    }

    for ( int i = 0 ; i < t_size*2-1 ; i++ ) {
        for ( int j = 0 ; j < t_size ; j++ ) {
            heights[ inputHeight[i][j] ]++;
        }
    }

    // find result
    int result[50];

    int count = 0;
    for ( int i = 0 ; i < 2500 ; i++ ) {
        if ( heights[i]%2 != 0 ) {
            if ( count >= t_size ) {
                cout << "ERROR!" << endl;
            }
            result[count] = i;
            count++;
        }
    }

    // for ( int i = 0 ; i < 2500 ; i++ ) {
    //     if ( heights[i] != 0 ) {
    //         cout << "RESULT::" << i << "::" << heights[i] << endl;
    //     }
    // }

    // output
    cout << "Case #" << number << ":";
    for ( int i = 0 ; i < t_size ; i++ ) {
        cout << " " << result[i];
    }
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

