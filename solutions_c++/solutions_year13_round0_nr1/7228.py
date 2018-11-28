#include <array>
#include <string>
#include <vector>

#include <stdio.h>
#include <stdlib.h>

#include <iostream>

using std::array;
using std::string;
using std::vector;

typedef int status;
typedef array<array<char,4>,4> board_data;
typedef vector<board_data> board_data_vector;

const status STATUS_WIN_X = 1;
const status STATUS_WIN_O = 2;
const status STATUS_DRAW = 3;
const status STATUS_ONGOING = 4;
const status STATUS_UNKNOWN = -1;

int decider(char symbol, int flag) { 
    int new_flag = 0;
    
    switch (symbol) {
        case '.':
            new_flag = -1;
            break;
        case 'X':
            if (flag == 0 || flag == 1) {
                new_flag = 1;
            } else {
                new_flag = -1;
            }
            break;
        case 'O':
            if (flag == 0 || flag == 2) {
                new_flag = 2;
            } else {
                new_flag = -1;
            }
            break;
        case 'T':
            // passtrough
            new_flag = flag;
            break;
        default:
            new_flag = -1;
            break;
    }

    return new_flag;
}

status flag_to_status(int flag) {
    
    switch (flag) {
        case 1:
            return STATUS_WIN_X;
        case 2:
            return STATUS_WIN_O;
        case 3:   
            return STATUS_DRAW;
        case 4:
            return STATUS_ONGOING;
        default:
            return STATUS_UNKNOWN;
    }
}

string status_to_string(int status) {
    switch (status) {
        case STATUS_WIN_X: return string("X won");
        case STATUS_WIN_O: return string("O won");
        case STATUS_DRAW: return string("Draw");
        case STATUS_ONGOING: return string("Game has not completed");
        default: return string("Out of range");
    }
}

board_data_vector * parse_input(vector<char> * input) {
    board_data_vector * all_boards = new board_data_vector();

    vector<char>::iterator it = input->begin();
    
    //skip numbers
    while ((*it)!='\n') {
        //std::cout << *it;
        it++;
    }
    //std::cout << " cases\n";
    //skip nl
    it++;

    while (it != input->end()) {
        board_data board;

        for (int i = 0; i<4; i++) {
            for (int j = 0; j<4; it++, j++) {
                board[i][j] = (*it);
            }
            //skip eol nl
            it++;
        }
        
        all_boards->push_back(board);
        //skip separating nl
        it++;
    }


    return all_boards;
}


status check_horizontal(board_data board) { 
    int flag = 0;

    for(int i=0; i<4 && ((flag==0) || (flag==-1)); i++) {

        flag = 0;
        char symbol = '\0';

        for(int j=0; (j<4) && (flag!=-1); j++) {
            symbol = board[i][j];
            
            flag = decider(symbol, flag);
        }
    }

    return flag_to_status(flag);
}

status check_vertical(board_data board) {
    int flag = 0;

    for(int j=0; j<4 && ((flag==0) || (flag==-1)); j++) {

        flag = 0;
        char symbol = '\0';

        for(int i=0; (i<4) && (flag!=-1); i++) {
            symbol = board[i][j];

            flag = decider(symbol, flag);
        }
    }

    return flag_to_status(flag);
}

//forward and backward
status check_diagonal(board_data board) {
    int flag = 0;
    char symbol = '\0';

    for(int i=0; (i<4) && (flag!=-1); i++) {
        symbol = board[i][i];

        flag = decider(symbol, flag);
    }
    
    if (flag == 0 || flag == -1) {
        flag = 0;
        symbol = '\0';

        for(int i=0, j=3; (i<4) && (flag!=-1); i++, j--) {
            symbol = board[i][j];
            //std::cout << symbol;
            flag = decider(symbol, flag);
            //std::cout << flag << "\n";
        }
    }

    return flag_to_status(flag);
}

status check_board_completed(board_data board) {
    //3 assumes full board
    int flag = 3;

    for (int i=0; i<4 && flag!=4; i++) {
        for (int j=0; j<4 && flag !=4; j++) {
            if(board[i][j] == '.') {
                flag = 4;
            }
        }
    
    }

    return flag_to_status(flag);
}

status check_status(board_data board) {
    status stat = STATUS_UNKNOWN;
    
    if ((stat = check_horizontal(board)) > 0) {
        return stat;
    } else {
        if ((stat = check_vertical(board)) > 0) {
            return stat;
        } else {
            if ((stat = check_diagonal(board)) > 0) {
                return stat;
            } else {
                return check_board_completed(board);
            }
        }
    }
}

int main() {
    char buffer[128];
    size_t bytes_read = 0;
    int bytes_read_total = 0;

    vector<char> * input = new vector<char>();

    while((bytes_read = fread(buffer, 1, sizeof(buffer), stdin)) > 0) {
        input->insert(input->end(), buffer, buffer+bytes_read);
        bytes_read_total += bytes_read;
    }
    // std::cout << "Read " << bytes_read_total << " characters\n";

    board_data_vector * all_boards;
    all_boards = parse_input(input);

    int count = 1;
    for (board_data_vector::iterator it = all_boards->begin(); it != all_boards->end(); ++it) {
        status stat = check_status(*it);
        
        string result = status_to_string(stat);
        std::cout << "Case #" << count << ": " << result << "\n";

        count++;
    }
    return 0;
}

