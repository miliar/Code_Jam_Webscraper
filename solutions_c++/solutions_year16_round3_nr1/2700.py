//
//  main.cpp / SenateEvacuation
//  CodeJam2016
//
//  문제: 정당 N개의 p1~pn 명의 국회의원이 있음
//      각 국회의원들을 최대 2명씩 밖으로 빼냄
//      다만 과반수는 없어야 함
//      A부터 Z까지 정당이 있음.
//  해법: 간단히, 가장 높은 수의 정당의 사람을 2명씩 뺀다.
//      정당별로 1명이 남을 때까지 다 뺀 뒤에
//      마지막 시점에 2개 정당의 각 1명씩이 남고 그걸 동시에 빼도록.
//      ..간단한데?
//

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void runQuestion(int number)
{

    // input
    int parties;
    cin >> parties;

    int senaters[26];
    int sumOfSenaters = 0;
    for ( int i = 0 ; i < parties ; i ++ ) {
        cin >> senaters[i];
        sumOfSenaters += senaters[i];
    }


    // preprocessing
    char partyname[26];
    for ( int i = 0 ; i < 26 ; i++ ) {
        partyname[i] = 'A'+i;
    }

    int major;
    int tmp;
    char tmpc;

    // for ( int i = 0 ; i < parties ; i++ ) {
    //     cout << partyname[i] << ":" << senaters[i] << ", " ;
    // }
    // cout << endl;

    for ( int i = 0 ; i < parties ; i++ ) {
        major = i;
        for ( int j = i+1 ; j < parties ; j++ ) {
            if ( senaters[j] > senaters[major] ) major = j;
        }

        tmp = senaters[i];
        senaters[i] = senaters[major];
        senaters[major] = tmp;

        tmpc = partyname[i];
        partyname[i] = partyname[major];
        partyname[major] = tmpc;
    }
    // 가장 큰 정당이 맨 앞으로 온다.
    // for ( int i = 0 ; i < parties ; i++ ) {
    //     cout << partyname[i] << ":" << senaters[i] << ", " ;
    // }
    // cout << endl;

    // output
    cout << "Case #" << number << ": " ;

    int lastSum = 0;
    int errorCode = 0;

    while (1) {
        lastSum = sumOfSenaters;
        // 파티를 돌면서
        if ( sumOfSenaters == 3 ) {
            cout << partyname[2] << " " ;
            sumOfSenaters --;
            senaters[2] --;
            parties --;
            continue;
        }

        else if ( sumOfSenaters == 2 ) {
            cout << partyname[0] << partyname[1];
            sumOfSenaters = 0;
            senaters[0] = senaters[1] = 0;
            parties = 0;
            break;
        }
        else if ( sumOfSenaters == 0 ) {
            break;
        }

        for ( int i = 0 ; i < parties-1 ; i++ ) {
            errorCode = 0;
            if ( senaters[i] >= senaters[i+1] + 2 ) {
                errorCode = 1;
                if ( i > 0 ) {
                    cout << partyname[i-1] << partyname[i];
                    senaters[i] --;
                    senaters[i-1] --;
                    sumOfSenaters -= 2;
                }
                else {
                    cout << partyname[i] << partyname[i];
                    senaters[i] -= 2;
                    sumOfSenaters -= 2;
                }
                break;  // 그리고 다시 앞에서 한다.
            }
            else if ( senaters[i] == senaters[i+1] + 1 ) {  // 하나 차이가 난다면
                errorCode = 2;
                // 다음 것 하나를 골라줍시다.
                cout << partyname[i];
                senaters[i] --;
                sumOfSenaters --;

                if ( senaters[i+1] == senaters[parties-1] ) // 다음 것과 마지막 것의 크기가 같다면
                {
                    errorCode = 3;
                    cout << partyname[parties-1];   // 마지막 거 하나 빼고
                    senaters[parties-1] --;
                    sumOfSenaters--;
                    if ( senaters[parties-1] == 0 ) {   // 다 나갔으면
                        errorCode = 4;
                        parties --;
                    }
                }
                else {
                    errorCode = 5;
                    // 그게 아니라면 중간에 차이가 있으니
                    for ( int j = i + 1 ; j < parties-1 ; j++ )  {
                        errorCode = 6;
                        if ( senaters[j] > senaters[j+1] ) {
                            cout << partyname[j];
                            senaters[j]--;
                            sumOfSenaters --;
                            break;
                        }
                    }

                }
                break;
            }
            else if ( senaters[i] == senaters[i+1] ) {  // 만약 같다면
                errorCode = 7;
                if ( senaters[i+1] == senaters[parties-1] ) { // 마지막 것과도 같다면
                    errorCode = 8;
                    // 끝까지 다 똑같은 숫자라서
                    // 맨 끝에서 한 개씩 빼자.
                    cout << partyname[parties-2] << partyname[parties-1];
                    senaters[parties-2]--;
                    senaters[parties-1]--;

                    sumOfSenaters -= 2;

                    if ( senaters[parties-1] == 0 ) {   // 다 나갔으면
                        parties --;
                    }
                    if ( senaters[parties-2] == 0 ) {
                        parties --;
                    }
                    break;
                }
                else {  // 마지막 게 다르다면, 같은 숫자를 쭉 따라가자.
                    errorCode = 9;
                    int current = senaters[i+1];
                    for ( int j = i+2 ; j < parties ; j++ ) {
                        if ( senaters[j] != current ) {
                            cout << partyname[j-1] << partyname[j-2];
                            senaters[j-1]--;
                            senaters[j-2]--;
                            sumOfSenaters -= 2;
                            break;
                        }
                    }
                }
                break;
            }
            // for ( int i = 0 ; i < parties ; i++ ) {
            //     cout << partyname[i] << ":" << senaters[i] << ", " ;
            // }
            // cout << endl;

        }
        cout << " " ;
        if ( lastSum == sumOfSenaters || sumOfSenaters < 0 ) {
            cout << "ERROR!" << errorCode ;
            break;
        }
    }   // while
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

