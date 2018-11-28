#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector> 
#include <cstdint>

using namespace std;

void flip(int idx, std::vector<bool> & pancakes) {
    for (int i = idx; i < pancakes.size(); i++) {
        pancakes[i] = !pancakes[i];
    }
}
        

int num_flips(std::vector<bool> & pancakes) {
    int flips = 0;
    for (int i = 0; i < pancakes.size(); i++) {
        if (!pancakes[i]) {
            flip(i, pancakes);
            flips++;
        }
    }
    return flips;
}

int main(int argc, char **argv) {
    int tests;
    cin >> tests;

    for (int i = 1; i <= tests; i++) {
        std::string sides;
        cin >> sides;

        std::vector<bool> pancakes;
        for (int i = sides.size() - 1; i >= 0; i--) {
            if (sides[i] == '+') {
                pancakes.emplace_back(true);
            } else {
                pancakes.emplace_back(false);
            }
        }

       
        cout << "Case #" << i << ": ";
        cout << num_flips(pancakes) << endl;
    }
    
    return 0;
}



