#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>


static void
parseArrange(int& rowSelected, int cards[4][4])
{
    std::cin >> rowSelected;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            std::cin >> cards[i][j];
        }
    }
}

static int
countRepetitions(int v1[4], int v2[4], int& rep)
{
    int count = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (v1[i] == v2[j]) {
                ++count;
                rep = v1[i];
            }
        }
    }
    
    return count;
}

int main(int argc, char** args)
{
    int count = 0;
    int row;
    int cards[4][4];
    int selected[4];
    
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
        // parse first arrange
        parseArrange(row, cards);
        // copy the selected
        for (int j = 0; j < 4; ++j) selected[j] = cards[row-1][j];
        
        // read the second one
        parseArrange(row, cards);
        
        // count repetitions (slow but it will be fast anyway)
        int card = 0;
        const int rep = countRepetitions(selected, cards[row-1], card);
        std::cout << "Case #" << i+1 << ": ";
        if (rep == 1) std::cout << card;
        else if (rep > 1) std::cout << "Bad magician!";
        else std::cout << "Volunteer cheated!";
        std::cout << "\n";   
    }
    
    
    return 0;
}
