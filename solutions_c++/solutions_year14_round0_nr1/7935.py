#include <iostream>
#include <set>

void readCards(int cards[4][4]) {
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            std::cin >> cards[r][c];
        }
    }
}

void processCase(int caseNumber) {
    int chosenRow1;
    std::cin >> chosenRow1;
    int cards1[4][4];
    readCards(cards1);
    
    std::set<int> possibleCards1;
    for (int i = 0; i < 4; i++) {
        possibleCards1.insert(cards1[chosenRow1-1][i]);
    }
    
    int chosenRow2;
    std::cin >> chosenRow2;
    int cards2[4][4];
    readCards(cards2);
    
    std::set<int> possibleCards2;
    for (int i = 0; i < 4; i++) {
        int card = cards2[chosenRow2-1][i];
        if (possibleCards1.count(card) == 1) {
            possibleCards2.insert(card);
        }
    }
    
    if (possibleCards2.size() == 1) {
        std::cout << "Case #" << caseNumber << ": " << *possibleCards2.begin() << std::endl;
    }
    else if (possibleCards2.size() > 1) {
        std::cout << "Case #" << caseNumber << ": Bad magician!" << std::endl;
    }
    else if (possibleCards2.size() == 0) {
        std::cout << "Case #" << caseNumber << ": Volunteer cheated!" << std::endl;
    }
}

int main() {
    int numberOfCases;
    std::cin >> numberOfCases;
    
    for (int i = 1; i <= numberOfCases; i++) {
        processCase(i);
    }
    
    return 0;
}

