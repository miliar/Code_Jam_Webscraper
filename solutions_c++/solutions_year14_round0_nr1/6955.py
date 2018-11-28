#include <iostream>

int main() {
    int cases;
    std::cin >> cases;
    for(int i = 0;i<cases;++i) {
        std::cout << "Case #" << i+1 << ": ";
        int choice1;
        std::cin >> choice1;
        int cards1[16];
        for(int j = 0;j<16;++j) {
           std::cin >> cards1[j];
        }
        
        int choice2;
        std::cin >> choice2;
        int cards2[16];
        for(int j = 0;j<16;++j) {
           std::cin >> cards2[j];
        }
    
        int rows[4] = {-1,-1,-1,-1};
        int cards[4] = {0,0,0,0};
        for(int k = 0;k<4;++k) {
            int card = cards1[4*(choice1-1)+k];
            int j = 0;
            for(;cards2[j]!=card;++j);
            int row = j/4;
            rows[row] = card;
            cards[row]++; 
        }
        
        if(cards[choice2-1]==0) {
            std::cout << "Volunteer cheated!\n";
        } else if(cards[choice2-1]>1) {
            std::cout << "Bad magician!\n";
        } else {
            std::cout << rows[choice2-1] << "\n";
        }

    }

	return 0;
}
