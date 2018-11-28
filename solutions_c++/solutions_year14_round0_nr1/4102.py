#include <iostream>

using namespace std;

int input();
int process();
int printResult();

int choice1, choice2;
int board1[4][4], board2[4][4];
int result;
int resultCase;
enum ResultCase{
    SOLVED,
    BAD_MAGICIAN,
    VOLUNTEER_CHEATED
};

int main ( void ){
    int i;
    int count;

    cin >> count;

    for( i = 0; i < count; i++ ){
        input();
        process();
        cout << "Case #" << i + 1 << ": ";
        printResult();
    }

    return 0;
}

int input(){
    int i, j;

    cin >> choice1;
    for( i = 0; i < 4; i++ ){
        for( j = 0; j < 4; j++ ){
            cin >> board1[i][j];
        }
    }

    cin >> choice2;
    for( i = 0; i < 4; i++ ){
        for( j = 0; j < 4; j++ ){
            cin >> board2[i][j];
        }
    }

    choice1--; choice2--;

    return 0;
}

int findDuplicated( int row1[4], int row2[4], int &count, int &number ){
    int i, j;

    count = 0;
    number = -1;
    for( i = 0; i <4; i++ ){
        for( j = 0; j < 4; j++ ){
            if( row1[i] == row2[j] ){
                count++;
                number = row1[i];
            }
        }
    }

    return 0;
}

int process(){
    int i, j;
    int count, number;
    result = -1;
    resultCase = SOLVED;

    findDuplicated( board1[choice1], board2[choice2], count, number );
    //cout << "count: " << count << endl;
    //cout << "number: " << number << endl;

    if( count == 0 ) resultCase = VOLUNTEER_CHEATED;
    else if( count > 1 ) resultCase = BAD_MAGICIAN;
    else if( count == 1 ){
        resultCase = SOLVED;
        result = number;
    }
    else cout << "---------- No Answer!! ----------------" << endl;

    return 0;
}

int printResult(){
    int i;
    
    if( resultCase == BAD_MAGICIAN ) cout << "Bad magician!";
    else if( resultCase == VOLUNTEER_CHEATED ) cout << "Volunteer cheated!";
    else if( resultCase == SOLVED ) cout << result; 
    else cout << "Can't find Solution!!";

    cout << endl;
    
    return 0;
}
