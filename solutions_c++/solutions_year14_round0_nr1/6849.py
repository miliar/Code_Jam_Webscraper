#include <iostream>

int main()
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        int answer1;
        std::cin >> answer1;
        --answer1;
        int arrange1[16];
        for (int j = 0; j < 16; ++j) {
            std::cin >> arrange1[j];
        }
        int answer2;
        std::cin >> answer2;
        --answer2;
        int arrange2[16];
        for (int j = 0; j < 16; ++j) {
            std::cin >> arrange2[j];
        }
        int result = 0;
        bool bad = false;
        for (int j = 0; j < 4; ++j) {
            int card1 = arrange1[answer1*4 + j];
            for (int k = 0; k < 4; ++k) {
                int card2 = arrange2[answer2*4 + k];
                if (card1 == card2) {
                    if (result == 0) {
                        result = card1;
                    } else {
                        bad = true;
                        goto quit;
                    }
                }
            }
        }
        quit:
        std::cout << "Case #" << (i + 1) << ": ";
        if (bad) {
            std::cout << "Bad magician!";
        }
        else if (result == 0) {
            std::cout << "Volunteer cheated!";
        }
        else {
            std::cout << result;
        }
        std::cout << "\n";
    }
    return 0;
}
