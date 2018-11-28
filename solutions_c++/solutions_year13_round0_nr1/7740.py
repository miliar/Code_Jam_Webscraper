#include <iostream>
#include <cstdio>

using namespace std;

int dp_row[4][4], dp_col[4][4], dp_di_1[4][4], dp_di_2[4][4];
int dp_support[4][4]; // 1 -> up, 2 -> left, 3-> diagonal
char TTT[4][4];
int values[] = {4 * 'W', 4 * 'O', 3 * 'W' + 'T', 3 * 'O' + 'T'};

int run_dp(){

    // Rowwise Winner
    for(int i = 0 ; i < 4 ; i++){

        char first_element = TTT[i][0];
        int count = 1, j_start = 1;

        // Impossible to find winner in this row
        if(first_element == '.')
            continue;

        // Only 1 'T' is possible
        if(first_element == 'T'){
            first_element = TTT[i][1];
            count = 2, j_start = 2;
        }

        for(int j = j_start ; j < 4 ; j++){
            if(TTT[i][j] == first_element || TTT[i][j] == 'T'){
                count++;
            }
        }

        if(count == 4){
            if(first_element == 'X')
                return 1;
            else if(first_element == 'O')
                return 2;
        }
    }

    // Columnwise Winner
    for(int j = 0 ; j < 4 ; j++){

        char first_element = TTT[0][j];
        int count = 1, i_start = 1;

        // Impossible to find winner in this row
        if(first_element == '.')
            continue;

        // Only 1 'T' is possible
        if(first_element == 'T'){
            first_element = TTT[1][j];
            count = 2, i_start = 2;
        }

        for(int i = i_start ; i < 4 ; i++){
            if(TTT[i][j] == first_element || TTT[i][j] == 'T'){
                count++;
            }
        }

        if(count == 4){
            if(first_element == 'X')
                return 1;
            else if(first_element == 'O')
                return 2;
        }
    }

    // Diagonal

    int value = TTT[0][0] + TTT[1][1] + TTT[2][2] + TTT[3][3];
    int winner = 3;
    bool won = false;

    // Diagonal 1
    for(int i = 0 ; i < 4 ; i++){
        if(value == values[i]){
            winner = i % 2;
            won = true;
        }
    }

    if(won) return winner + 1;

    // Diagonal 2
    value = TTT[0][3] + TTT[1][2] + TTT[2][1] + TTT[3][0];
    winner = 3, won = false;

    for(int i = 0 ; i < 4 ; i++){
        if(value == values[i]){
            winner = i % 2;
            won = true;
        }
    }

    if(won) return winner + 1;

    return 0;
}


int main()
{
    int cases;
    char ch;
    char line[4];

    bool has_dot;

    scanf("%d",&cases);
    scanf("%c",&ch);

    for(int index = 0 ; index < cases; index++){

        has_dot = false;

        // Take Input 4 * 4 array
        for(int i = 0 ; i < 4 ; i++){
            gets(line);

            for(int j = 0 ; j < 4 ; j++){
                TTT[i][j] = line[j];
                if(line[j] == '.')
                    has_dot = true;
            }
        }

        scanf("%c",&ch);

        int winner = run_dp();

        if(winner){
            // Winner is 'X'
            if(winner == 1){
                printf("Case #%d: X won\n",index+1);
            }
            // Winner is 'O'
            else{
                printf("Case #%d: O won\n",index+1);
            }
        }
        // We have got no winner
        else{
            // Game is not over
            if(has_dot){
                printf("Case #%d: Game has not completed\n",index+1);
            }
            // Draw
            else{
                printf("Case #%d: Draw\n",index+1);
            }
        }
    }

    return 0;
}
