#include <iostream>
#include <vector>

int main() {
    int t = 0;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::vector<std::vector<int> > board(4, std::vector<int>(4,0));
        bool hasempty = false;
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                // X = 1
                // O = -1
                // T = 100
                char c;
                std::cin >> c;
                
                if (c == 'T') {
                    board[j][k] = 100;
                }
                
                if (c == 'O') {
                    board[j][k] = -1;
                }
                if (c == 'X') {
                    board[j][k] = 1;
                }
                if (c == '.') {
                    hasempty = true;
                }

            }
        }
        bool exit = false;
        for (int j = 0; j < 4; ++j) {
            int x = board[j][0] + board[j][1] + board[j][2] + board[j][3];
            int y = board[0][j] + board[1][j] + board[2][j] + board[3][j]; 
            if (x == 103 || x == 4 || y == 103 || y == 4) {
                std::cout << "Case #" << i+1 << ": X won\n";
                exit = true;
                break;
            }
            if (x == 97 || x == -4 || y == 97 || y == -4) {
                std::cout << "Case #" << i+1 << ": O won\n";
                exit = true;
                break;
            }
        }
        if (exit) {
		char c[2];
		std::cin.getline (c,2);
            continue;
		}
        
        int x = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        int y = board[3][0] + board[2][1] + board[1][2] + board[0][3];
        if (x == 103 || x == 4 || y == 103 || y == 4) {
                std::cout << "Case #" << i+1 << ": X won\n";
                exit = true;
                //break;
            }
        if (x == 97 || x == -4 || y == 97 || y == -4) {
                std::cout << "Case #" << i+1 << ": O won\n";
                exit = true;
                //break;
            }
        if (exit) {
		char c[2];
		std::cin.getline (c,2);
            continue;
		}
        if (hasempty) { 
            std::cout << "Case #" << i+1  << ": Game has not completed\n";
		char c[2];
		std::cin.getline (c,2);	            
		continue;
        } else {
            std::cout << "Case #" << i+1  << ": Draw\n";
        } 
		char c[2];
		std::cin.getline (c,2);


    }
    return 0;
}
