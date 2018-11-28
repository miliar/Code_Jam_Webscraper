#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main(int argc, char *argv[])
{
    int cases = 0;
    std::cin >> cases;

    std::cin.clear();
    std::cin.ignore();

    for(int i = 0; i < cases; i++)
    {
        // answer to first question
        int answer;
        int answer2;
        std::cin >> answer;

        int cards[4][4];
        int cards2[4][4];

        for(int j = 0; j < 4; j++)
        {
            std::cin >> cards[0][j] >> cards[1][j] >> cards[2][j] >> cards[3][j];
        }

        std::cin >> answer2;

        for(int j = 0; j < 4; j++)
        {
            std::cin >> cards2[0][j] >> cards2[1][j] >> cards2[2][j] >> cards2[3][j];
        }

        if(answer > 4 || answer2 > 4 || answer < 1 || answer2 < 1)
            continue;

        std::vector <int> found;

        for(int j = 0; j < 4; j++)
        {
            for(int l = 0; l < 4; l++)
            {
                if(cards[j][answer-1] == cards2[l][answer2-1])
                    found.push_back(cards[j][answer-1]);
            }
        }

        std::cout << "Case #" << i+1 << ": ";
        if(found.size() == 1)
            std::cout << found[0];
        else if(found.size() > 1)
            std::cout << "Bad magician!";
        else
            std::cout << "Volunteer cheated!";

        std::cout << std::endl;
    }
}


