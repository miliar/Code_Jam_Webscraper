#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    int testcases;
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    input >> testcases;
        for (int i= 0; i < testcases; i++){
        int answer1;
        int possiblecards[16] = {0};
        input >> answer1;
            for (int c = 1; c < 5; c++){
                for (int y = 1; y < 5; y++){
                int check;
                input >> check;
                    if (c == answer1){
                    possiblecards[check-1] = 1;
                    }
                }
            }
        int answer2;
        input >> answer2;
            for (int c = 1; c < 5; c++){
                for (int y = 1; y < 5; y++){
                int check;
                input >> check;
                    if (c == answer2){
                    possiblecards[check-1] = possiblecards[check-1] + 1;
                    }
                }
            }
        int answers = 0;
        int lastpos;
            for (int z = 0; z < 16; z++){
                if (possiblecards[z] == 2){
                answers++;
                lastpos = z+1;
                }
            }
            if (answers == 0){
            output << "Case #" << i+1 << ": Volunteer cheated!" << endl;
            } else if (answers == 1) {
            output << "Case #" << i+1 << ": " << lastpos << endl;
            } else {
            output << "Case #" << i+1 << ": Bad magician!" << endl;
            }
        }
    return 0;
}
