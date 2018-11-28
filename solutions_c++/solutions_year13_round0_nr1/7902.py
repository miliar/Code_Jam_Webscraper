#include <iostream>
#include <string>

enum state {XWON = 0, OWON, NCOM, DRAW, UNDEF};

int main()
{

    int n, nt;

    std::cin >> n;

   // std::cout << "Test cases: " << n << std::endl;

    std::string line;

    int board[4][4];

    nt = n;
    while(n--){

        bool mayNotComp = false;

        // Read test case
        for(int i = 0; i < 4; i++){

            std::cin >> line;
           // std::cout << line << std::endl;

            for(int j = 0; j < 4; j++){
                if(line[j] == 'X'){
                    board[i][j] = 3;
                }else if(line[j] == 'O'){
                    board[i][j] = -3;
                }else if(line[j] == 'T'){
                    board[i][j] = 1;
                }else{
                    mayNotComp = true;
                    board[i][j] = 0;
                }
            }
        }

        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                //std::cout << board[i][j] << "\t";
            }
           // std::cout << std::endl;
        }

        // Do work
        state game = UNDEF;
        int s = 0, s2 = 0;

        for(int i = 0; i < 4 && game == UNDEF; i++){
            s = 0;
            s2 = 0;
            for(int j = 0; j < 4; j++){
                s += board[i][j];
                s2 += board[j][i];
            }
            //std::cout << "S: " << s << ", S2: " << s2 << std::endl;
            if(s == 12 || s == 10 || s2 == 12 || s2 == 10){
                game = XWON;
            }else if(s == -12 || s == -8 || s2 == -12 || s2 == -8){
                game = OWON;
            }
        }
        s = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        s2 = board[0][3] + board[1][2] + board[2][1] + board[3][0];
        if(s == 12 || s == 10 || s2 == 12 || s2 == 10){
            game = XWON;
        }else if(s == -12 || s == -8 || s2 == -12 || s2 == -8){
            game = OWON;
        }
        if(game == UNDEF){
            if(mayNotComp){
                game = NCOM;
            }else{
                game = DRAW;
            }
        }

        // Write solution
        std::cout << "Case #" << nt -n << ": ";
        switch (game) {
        case XWON:
            std::cout << "X won";
            break;
        case OWON:
            std::cout << "O won";
            break;
        case DRAW:
            std::cout << "Draw";
            break;
        case NCOM:
            std::cout << "Game has not completed";
            break;
        default:
            break;
        }
        std::cout << std::endl;
    }

    return 0;
}

