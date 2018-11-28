//
//  main.cpp
//  CodeJamQ1
//
//  Created by Ethan Gill on 4/10/15.
//  Copyright (c) 2015 Ethan Gill. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int convertChar(char a){
    int ia = a - '0';
    return ia;
}

int main(int argc, const char * argv[]) {
    ifstream exprFile(argv[1]);
    int casesCount;
    int caseCounter = 1;
    exprFile >> casesCount;
    //cin >> casesCount;
    for (int i = 0; i < casesCount; i++) {
        //for each case
        string problem;
		//twice 
		exprFile >> problem;
        exprFile >> problem;
        int standersCount = 0;
        int neededCount = 0;
        //initial case
        for (int j = 0; j < problem.size(); j++) {
            while (standersCount < j) {
                standersCount++;
                neededCount++;
            }
            standersCount += convertChar(problem.at(j));
        }
        cout << "Case #" << caseCounter << ": " << neededCount << endl;
        caseCounter++;
    }
    return 0;
}
