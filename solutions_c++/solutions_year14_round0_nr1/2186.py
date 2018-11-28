#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{   ofstream output;
    output.open ("solved.out");
    ifstream input("test.in");
    int test_cases;
    input >> test_cases;
    for (int z = 0; z < test_cases; z++) {
    int row;
    input >> row;
    vector<int> cards;
    int card;

        for (int i = 0; i < 16; i++) {
                input >> card;
         if (i >= 4*(row-1) && i < 4*row) {
            cards.push_back(card);

    }
        }

    int row2;
    input >> row2;
    vector<int> cards2;
    int card2;

        for (int i = 0; i < 16; i++) {
            input >> card2;
         if (i >= 4*(row2-1) && i < 4*row2) {
            cards2.push_back(card2);

    }
        }



    int counter = 0;
    int answer;
    for (int x : cards) {
        for (int y : cards2) {
            if ( x== y) {
                answer = x;
                counter++;
            }
        }
    }

    if (counter==1) {
        output << "Case #" << z+1 << ": "  << answer << endl;
    }

    if (counter > 1) {
       output << "Case #" << z+1 << ": "  << "Bad magician!" << endl;
    }

    if (counter == 0) {
        output << "Case #" << z+1 << ": "  << "Volunteer cheated!" << endl;
    }
    }

    return 0;
}
