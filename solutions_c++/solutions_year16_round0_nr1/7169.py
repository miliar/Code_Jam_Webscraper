//
//  main.cpp
//  [CodeJam] - Problem A
//
//  Created by Vlad Dascalu on 09/04/16.
//  Copyright © 2016 Vlad Dascalu. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream f ("input.txt");
ofstream g ("/Users/Vlad/Desktop/output.txt");

bool digits[10];

void addDigits(int number) {
    while (number) {
        digits[number%10] = true;
        number /= 10;
    }
}

bool isComplete() {
    for (int i = 0; i < 10; i++) {
        if (digits[i] == false) {
            return false;
        }
    }
    return true;
}

void ResetDigits() {
    for (int i = 0; i < 10; i++) {
        digits[i] = false;
    }
}

long int LastNumber(int number, int stage) {
    if (number == 0) {
        return -1;
    }
    addDigits(number);
    if (isComplete()) {
        return number;
    }
    return LastNumber(number + stage, stage);
}

int main(int argc, const char * argv[]) {
    int N, i = 1, nr;
    long int lastNumber;
    f>>nr;
    while (i <= nr) {
        f>>N;
        lastNumber = LastNumber(N, N);
        if (lastNumber != -1) {
            g<<"Case #"<<i<<": "<<lastNumber<<endl;
        }
        else {
            g<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        ResetDigits();
        i++;
    }
    return 0;
}
