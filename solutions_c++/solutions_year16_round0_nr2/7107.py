#include <iostream>

using namespace std;

bool isAllBlank(string pancakes);
bool isAllHappy(string pancakes);
void flip(string &pancakes, int length);
char flipPancake(char pancake);

int main() {
    int testCases, maneuvers, index;
    string pancakes;

    cin >> testCases;
    for(int i = 1; i <= testCases; i++) {
        cin >> pancakes;
        maneuvers = 0;
        while(!isAllHappy(pancakes)) {
            if(isAllBlank(pancakes)) {
                flip(pancakes, pancakes.length());
                maneuvers++;
            } else {
                index = 1;
                while(pancakes[index] == pancakes[0]) {
                    index++;
                }
                flip(pancakes, index);
                maneuvers++;
            }
        }
        cout << "Case #" << i << ": " << maneuvers << endl;
    }

    return 0;
}

bool isAllBlank(string pancakes) {
    for(unsigned int i = 0; i < pancakes.length(); i++) {
        if(pancakes[i] == '+') {
            return false;
        }
    }
    return true;
}

bool isAllHappy(string pancakes) {
    for(unsigned int i = 0; i < pancakes.length(); i++) {
        if(pancakes[i] == '-') {
            return false;
        }
    }
    return true;
}

void flip(string &pancakes, int length) {
    char aux;
    int mid;

    if(length == 1) {
        pancakes[length - 1] = flipPancake(pancakes[length - 1]);
    } else {
        mid = 1 + (length - 1) / 2;
        for(int i = 0; i < mid; i++) {
            aux = pancakes[i];
            pancakes[i] = flipPancake(pancakes[length - i - 1]);
            pancakes[length - i - 1] = flipPancake(aux);
        }
    }
}

char flipPancake(char pancake) {
    if(pancake == '+') {
        return '-';
    } else {
        return '+';
    }
}
