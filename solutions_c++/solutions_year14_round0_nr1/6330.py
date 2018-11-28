

#include <iostream>


void readRows(int row[]) {
    int selectedRow;
    std::cin >> selectedRow;

    for (int currentRow = 0; currentRow<4; currentRow++) {
        int c1, c2, c3 ,c4;
        std::cin >> c1 >> c2 >> c3 >> c4;
        if(currentRow == selectedRow-1) {
            row[0] = c1; row[1] = c2; row[2] = c3; row[3] = c4;
        }
    }
}

int main(int argc, const char * argv[])
{
    int numberOfGames;
    std::cin >> numberOfGames;
    
    for (int gameNumber = 0; gameNumber<numberOfGames; gameNumber++) {
    
        std::cout << "Case #" << (gameNumber+1) << ": ";
        
        int firstRow[4];
        int secondRow[4];

        readRows(firstRow);

        readRows(secondRow);

        
        int matchedNumber = 0;
        int matchCount = 0;
        for (int f = 0; f<4; f++) {
            for (int s = 0; s<4; s++) {
                if(firstRow[f] == secondRow[s]) {
                    matchCount++;
                    matchedNumber = firstRow[f];
                }
            }
        }
        
        if(matchCount == 0 ) {
            std::cout << "Volunteer cheated!" << std::endl;
        } else if(matchCount == 1) {
            std::cout << matchedNumber << std::endl;
        } else if(matchCount > 1) {
            std::cout << "Bad magician!" << std::endl;
        }
    }


    return 0;
}

