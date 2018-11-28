#include <iostream>
#include <string>
#include <algorithm>

int main() {

    int noc;
    std::string empty;

    std::cin >> noc;
    for(int i = 0; i < noc; i++) {
        int X, Y;
        std::cin >> X;
        std::cin >> Y;
        int input[X][Y];

        for (int j = 0; j < X; j++) {
            for (int k = 0; k < Y; k++) {
                std::cin >> input[j][k];
            }
        }

        bool possible = true;
        for (int j = 0; j < X; j++) {
            for (int k = 0; k < Y; k++) {

                bool highest_in_row = true;
                for (int xx = 0; xx < Y; xx++) {
                    if (xx == k) continue;
                    if (input[j][xx] > input[j][k]) {
                        highest_in_row = false;
                        break;
                    }
                }
                bool highest_in_col = true;
                for (int xx = 0; xx < X; xx++) {
                    if (xx == j) continue;
                    if (input[xx][k] > input[j][k]) {
                        highest_in_col = false;
                        break;
                    }
                }

                if (!highest_in_col && !highest_in_row) {
                    possible = false;
                    break;
                }
            }
            if (possible == false) break;
        }

        if (possible == false) std::cout << "Case #" << i + 1 << ": NO\n";
        else std::cout << "Case #" << i + 1 << ": YES\n";
    }
}
