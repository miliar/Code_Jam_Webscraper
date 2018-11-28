
#include <iostream>
#include <string>

#define NON  0
#define X    8
#define O    9

using namespace std;

bool is_win(int num, bool has_t) {
    if (num == 4 || (num == 3 && has_t)) {
        return true;
    } else {
        return false;
    }
}

void update_param(char cur, int &x_num, int &o_num, bool &has_t) {
    if (cur == '.') {
        return ;
    } else if (cur == 'T') {
        has_t = true;
    } else if (cur == 'X') {
        x_num ++;
    } else if (cur == 'O') {
        o_num ++;
    }
}

void init_param(int &x_num, int &o_num, bool &has_t) {
    x_num = 0;
    o_num = 0;
    has_t = false;
}

int check_win(char (*board)[4]) {
    bool has_t = false;
    int x_num  = 0;
    int o_num  = 0;
    for(int i = 0; i < 4; i ++) {
        init_param(x_num, o_num, has_t);
        for(int j = 0; j < 4; j ++) {
            // check row
            update_param(board[i][j], x_num, o_num, has_t);
        }
        if (is_win(x_num, has_t)) {
            return X;
        } else if (is_win(o_num, has_t)) {
            return O;
        } else {
            init_param(x_num, o_num, has_t);
            
            for(int j = 0; j < 4; j ++) {
                // check column
                update_param(board[j][i], x_num, o_num, has_t);
            }
            if (is_win(x_num, has_t)) {
                return X;
            } else if (is_win(o_num, has_t)) {
                return O;
            }
        }
    }
    
    init_param(x_num, o_num, has_t);
    // check diagnal direction
    for(int i = 0; i < 4; i ++) {
        update_param(board[i][i], x_num, o_num, has_t);
    }
    if (is_win(x_num, has_t)) {
        return X;
    } else if (is_win(o_num, has_t)) {
        return O;
    }
    
    init_param(x_num, o_num, has_t);
    for(int i = 0; i < 4; i ++) {
        update_param(board[i][3-i], x_num, o_num, has_t);
    }
    if (is_win(x_num, has_t)) {
        return X;
    } else if (is_win(o_num, has_t)) {
        return O;
    } else {
        return NON;
    }
}

int main(int argc, const char * argv[])
{
    int cases = 0;
    std::cin >> cases;
    for(int run = 1; run <= cases; run ++) {
        char board[4][4] = {'.'};
        bool is_end = true;
        for(int i = 0; i < 4; i ++) {
            string line;
            std::cin >> line ;
            for(int j = 0 ; j < line.size(); j ++) {
                board[i][j] = line[j];
                if (board[i][j] == '.') {
                    is_end = false;
                }
            }
        }
        
        int status = check_win(board);
        std::cout << "Case #" << run << ": ";
        if (status == X) {
            std::cout << "X won" << std::endl;
        } else if (status == O) {
            std::cout << "O won" << std::endl;
        } else if (is_end == true && status == NON) {
            std::cout << "Draw" << std::endl;
        } else {
            std::cout << "Game has not completed" << std::endl;
        }
        
    }
    return 0;
}
