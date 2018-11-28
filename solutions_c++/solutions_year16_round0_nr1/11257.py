//
//  main.cpp
//  CodeJam
//
//  Created by Sahar Mostafa (Intel) on 4/9/16.
//  Copyright © 2016 Sahar Mostafa. All rights reserved.
//

#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <fstream>

#define MAX_COUNT 100

std::map<int, int> seen;

bool seenAll() {
    for (int k = 0; k < 10; k++)
        if(seen[k] == 0)
            return false;
    return true;
}

void seenNum(int num) {
    std::string result;
    std::stringstream convert;
    int i;
    convert << num;
    
    result = convert.str();
    for (i = 0; i < result.length(); i++) {
        int n = (char)result[i] - '0';
        std::map<int, int>::iterator it = seen.find(n);
        seen[n] = 1;
    }
}

int main(int argc, const char * argv[]) {
    int T = 1;
    int N = 1;
    int k = 0;
    int prev = 0;
    std::string result;
    int inputN[MAX_COUNT];

    // read input
    std::ifstream inFile("input.txt");
    bool firstLine = true;
    std::string line;
    while (std::getline(inFile, line))
    {
        std::istringstream iss(line);
        if(firstLine) {
            iss >> T;
            firstLine = false;
            continue;
        }
       
        iss >> inputN[k++];
    }
    inFile.close();

    for (int i = 0; i < T; i++)
    {
        N = inputN[i];
        k = 1;
        seen.clear();
        while (!seenAll()) {
            result = std::to_string(k*N);
            seenNum(k * N);
            k++;
            if (prev == k*N) {
                result = "INSOMNIA";
                break; //infinity and beyond
            }
            prev = k*N;
        }
        std::cout << "Case #" << i + 1 << ": " << result << "\n";
    }
    return 0;
}

