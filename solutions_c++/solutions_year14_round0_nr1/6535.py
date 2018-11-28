// clang++ -std=c++11 -stdlib=libc++ -Wall -o magic magic.cpp
// ./magic < input-small.txt 2>log.txt 1>small.out

#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
    int size;
    int board[2][4];
    
    cin >> size;
    for (int index = 1; index <= size; ++index) {
        cerr << "\nCase #" << index << '\n'; 
        for (int i = 0; i < 2; ++i) {
            int row = 0;
            cin >> row;
            cerr << row << '\n';
            row -= 1;
            for (int r = 0; r < 4; ++r) {
                if (r == row) {
                    for (int k = 0; k < 4; ++k) {
                        cin >> board[i][k];
                        cerr << board[i][k] << " ";
                    }
                    cerr << '\n';
                }
                else {
                    int null = 0;
                    for (int k = 0; k < 4; ++k) {
                        cin >> null;
                    }
                }
            }
        }

        int number = 0;
        int counter = 0;
        for (int i = 0; i < 4; ++i) {
            int value = board[0][i];
            for (int k = 0; k < 4; ++k) {
                if (value == board[1][k]) {
                    number = value;
                    counter++;
                }
            }
        }
        if (number == 0) {
            cout << "Case #" << index << ": Volunteer cheated!\n";
            cerr << "Case #" << index << ": Volunteer cheated!\n";
            continue;
        }
        if (counter > 1) {
            cout << "Case #" << index << ": Bad magician!\n";
            cerr << "Case #" << index << ": Bad magician!\n";
            continue;
        }
        cout << "Case #" << index << ": " << number << "\n";
        cerr << "Case #" << index << ": " << number << "\n";
    }
}
        
