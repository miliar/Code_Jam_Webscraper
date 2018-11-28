//
//  main.cpp
//  [CodeJam] - Problem B
//
//  Created by Vlad Dascalu on 09/04/16.
//  Copyright © 2016 Vlad Dascalu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream f ("input");
ofstream g ("/Users/Vlad/Desktop/output");

vector<char> stringToVector(char str[])
{
    vector<char> pancakes;
    int i = 0;
    while (str[i] != '\0') {
        pancakes.push_back(str[i]);
        i++;
    }
    return pancakes;
}

bool isHappy(vector<char> &pancakes) {
    vector<char>::iterator it = pancakes.begin();
    while (it != pancakes.end()) {
        if (*it == '-') {
            return false;
        }
        it++;
    }
    return true;
}

void FlipPancakes(vector<char> &pancakes, unsigned int number, char face) {
    unsigned int i = 0;
    while (i < number) {
        if (face == '+') {
            pancakes[i] = '-';
        }
        else {
            pancakes[i] = '+';
        }
        i++;
    }
}

unsigned int FlipPancakes(vector<char> & pancakes) {
    unsigned int count = 0;
    while (!isHappy(pancakes)) {
        char a = *pancakes.begin();
        unsigned int i = 1;
        while (pancakes[i] == a && i < pancakes.size()) {
            i++;
        }
        FlipPancakes(pancakes, i, a);
        count++;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    int T, i = 1;
    char S[101];
    f>>T;
    while (i <= T) {
        f>>S;
        vector<char> string = stringToVector(S);
        int numberOfFlips = FlipPancakes(string);
        g<<"Case #"<<i<<": "<<numberOfFlips<<endl;
        i++;
    }
    return 0;
}
