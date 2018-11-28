#include <iostream>
#include <vector>

void fillMatrix(std::istream & in, int * matrix);
std::vector<int> possibleCards(int * cards, int row);

int main() {
    int T;
    int cards[16];
    int row;

    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        std::cin >> row;
        fillMatrix(std::cin, cards);
        std::vector<int> firstPossible = possibleCards(cards, row);

        std::cin >> row;
        fillMatrix(std::cin, cards);
        std::vector<int> secondPossible = possibleCards(cards, row);

        int matches = 0;
        int lastmatch = 0;
        for (int j: firstPossible) {
            for (int k: secondPossible) {
                if (j == k) {
                    ++matches;
                    lastmatch = j;
                }
            }
        }

        if (matches == 0) std::cout << "Case #" << i + 1 << ": Volunteer cheated!\n";
        else if (matches == 1) std::cout << "Case #" << i + 1 << ": " << lastmatch << std::endl;
        else if (matches > 1) std::cout << "Case #" << i + 1 << ": Bad magician!\n";
    }
}
 
void fillMatrix(std::istream & in, int * matrix) {
    for (int i = 0; i < 16; ++i) std::cin >> matrix[i];
}

std::vector<int> possibleCards(int * cards, int row) {
    std::vector<int> possible;
    for (int i = 0; i < 4; ++i) {
        possible.push_back(cards[ (row - 1) * 4 + i ]);
    }
    return possible;
}  
