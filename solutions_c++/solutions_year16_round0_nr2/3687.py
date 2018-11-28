/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex
 *
 * Created on 2016年4月9日, 下午 5:21
 */

#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

/*
 * 
 */

bool CheckSolve(string& stackOfCakes) {
    for(int i = 0; i < stackOfCakes.size(); i++) {
        if(stackOfCakes[i] == '-')
            return false;
    }

    return true;
}

void Flip(string& stackOfCakes, int index) {
    for(int i=0; i < index; i++) {
        if(stackOfCakes[i] == '+')
            stackOfCakes.replace(i, 1, 1,'-');
        else
            stackOfCakes.replace(i, 1, 1,'+');
    }
    reverse(stackOfCakes.begin(), stackOfCakes.begin() + index);

    return;
}

int FindIndex(string& stackOfCakes) {
    int index = -1;
    for(int i = 0; i < stackOfCakes.size(); i++) {
        if(stackOfCakes[0] == '+' && stackOfCakes[i] == '-') {
            index = i - 1;
            break;
        }
        else if(stackOfCakes[0] == '-' && stackOfCakes[i] == '-')
            index = i;
        else if(index >= 0)
            break;
    }

    return index;
}

void Solve() {
    int total;
    scanf("%d", &total);

    for(int i = 0; i < total; i++) {
        string stackOfCakes;
        cin >> stackOfCakes;
        printf("Case #%d: ", i+1);
        int step = 0;
        while(!CheckSolve(stackOfCakes)) {
            int flipIndex = FindIndex(stackOfCakes);
            Flip(stackOfCakes, flipIndex + 1);
            step++;
        }
        printf("%d\n", step);
    }

    return;
}

int main(int argc, char** argv) {
    Solve();

    return 0;
}

