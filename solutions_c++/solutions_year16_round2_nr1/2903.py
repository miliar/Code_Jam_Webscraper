//
//  main.cpp / PhoneNumber
//  CodeJam2016
//
//  문제: 정해진 숫자를 영어로 바꾸고 > 대문자로 바꾼 뒤 > 합쳐서 > 섞었다.
//      원래 숫자는 뭘까?
//  해법: 들어있는 글자들을 전부 읽어서 개수를 세고, 거기서 순서대로 뽑아내면 됨.
//      예를 들어 ZERO가 2 개 있다면 전체 배열에서 Z, E, R, O 를 두 개씩 뽑으면 됨.
//      기본적으로 이 룰에서 몇 가지 장점이 있는데..
//      1) Z 는 ZERO 에만 있다.
//      2) W 는 TWO 에만 있다.
//      3) X 는 SIX 에만 있다.
//      4) G 는 EIGHT 에만.
//      5) S 는 six 를 빼면 seven 에만 있다
//      6) V 는 seven 을 빼면 five 에만 있다
//      7) F 는 five 를 빼면 four 에만 있다
//      8) R 은 four 와 zero 를 빼면 three 에만 있다.
//      9) I 는 nine 에만, five, six, eight.
//      10) 남은 건 다 one.
//      증명 종료.
//  해결법)
//      1) S에서 모든 글자에 array에 +1
//      2) 0~9 까지의 저장된 배열에서 순서대로 숫자를 빼내간다.
//      3) 빼내면서 0~9 까지의 숫자를 +1
//      4) 결과 출력
//

#include <iostream>
#include <string>
#include <sstream>

using namespace std;


void runQuestion(int number)
{

    // input
    char inputString[2002];
    cin >> inputString;

    // preset
    int order[10] = {0, 2, 6, 8, 7, 5, 4, 3, 9, 1};
    int result[10];
    int inputStringData[26];
    for ( int i = 0 ; i < 26 ; i++ ) {
        inputStringData[i] = 0;
    }
    for ( int i = 0 ; i < 10 ; i++ ) {
        result[i] = 0;
    }

    /*
    int characterData[10][26];
    char numberChar[10][6];
    strcpy(numberChar[0], "ZERO");
    strcpy(numberChar[1], "ONE");
    strcpy(numberChar[2],"TWO");
    strcpy(numberChar[3], "THREE");
    strcpy(numberChar[4], "FOUR");
    strcpy(numberChar[5], "FIVE");
    strcpy(numberChar[6], "SIX");
    strcpy(numberChar[7], "SEVEN");
    strcpy(numberChar[8], "EIGHT");
    strcpy(numberChar[9], "NINE");

    for ( int i = 0 ; i < 10 ; i ++ ) {
        for ( int j = 0 ; j < 26 ; j++ ) {
            characterData[i][j] = 0;
        }
    }

    for ( int i = 0 ; i < 10 ; i ++ ) {
        for ( int j = 0 ; j < strlen(numberChar[i]) ; j++ ) {
            characterData[i][numberChar[i][j] - 'A'] ++;
        }
    }

    for ( int i = 0 ; i < 10 ; i ++ ) {
        cout << " { " ;
        for ( int j = 0 ; j < 26 ; j++ ) {
            if ( j != 0 ) cout << ",";
            cout << characterData[i][j];
        }
        cout << " }, " <<  endl;
    }
    */
   // {0, 2, 6, 8, 7, 5, 4, 3, 9, 1};
   // //      1) Z 는 ZERO 에만 있다.
//      2) W 는 TWO 에만 있다.
//      3) X 는 SIX 에만 있다.
//      4) G 는 EIGHT 에만.
//      5) S 는 six 를 빼면 seven 에만 있다
//      6) V 는 seven 을 빼면 five 에만 있다
//      7) F 는 five 를 빼면 four 에만 있다
//      8) R 은 four 와 zero 를 빼면 three 에만 있다.
//      9) I 는 nine 에만, five, six, eight.
//      10) 남은 건 다 one.

    int characterData[10][27] = {
         { 26, 0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1 },
         { 5 , 0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0 },
         { 23, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0 },
         { 18, 0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0 },
         { 6 , 0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0 },
         { 22, 0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0 },
         { 24, 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0 },
         { 19, 0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0 },
         { 7 , 0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0 },
         { 9 , 0,0,0,0,1,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0 }
    };

    // setting
    for ( int i = 0 ; i < strlen(inputString) ; i++ ) {
        inputStringData[ inputString[i]-'A' ] ++ ;
    }

    // processing
    for ( int i = 0 ; i < 10 ; i++ ) {
        int nextNumber = order[i];
        int targetCharacter = characterData[nextNumber][0] - 1;
        int targetCount = inputStringData[targetCharacter];
        result[nextNumber] = targetCount;

        for ( int j = 0 ; j < 26 ; j ++ ) {
            inputStringData[j] -= characterData[nextNumber][j+1] * targetCount;
        }
    }

    // output
    cout << "Case #" << number << ": ";

    for ( int i = 0 ; i < 10 ; i ++ )  {
        for ( int j = 0 ; j < result[i] ; j++ )
            cout << i ;
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

