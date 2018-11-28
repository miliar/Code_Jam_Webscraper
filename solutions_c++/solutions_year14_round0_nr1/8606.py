#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>


int main()
{
    auto& in = std::cin;
    auto& out = std::cout;

    size_t T;
    in >> T;
    for (size_t t = 0; t < T; ++t) {
        size_t row1;
        in >> row1;
        --row1;
        size_t grid1[4][4];
        for (size_t r = 0; r < 4; ++r) {
            for (size_t c = 0; c < 4; ++c) {
                size_t card;
                in >> card;
                grid1[r][c] = card;
            }
        }

        size_t row2;
        in >> row2;
        --row2;
        size_t grid2[4][4];
        for (size_t r = 0; r < 4; ++r) {
            for (size_t c = 0; c < 4; ++c) {
                size_t card;
                in >> card;
                grid2[r][c] = card;
            }
        }
        
        size_t counter = 0;
        size_t card = size_t(-1);
        for (size_t c1 = 0; c1 < 4; ++c1) {
            size_t card1 = grid1[row1][c1];
            for (size_t c2 = 0; c2 < 4; ++c2) {
                size_t card2 = grid2[row2][c2];
                if (card1 == card2) {
                    ++counter;
                    card = card2;
                    break;
                }
            }
        }
        out << "Case #" << (t + 1) << ": ";
        if (counter == 1) {
            out << card;
        } else if (counter == 0) {
            out << "Volunteer cheated!";
        } else {
            out << "Bad magician!";
        }
        out << std::endl;
    }    
    return 0;
}

