//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Momo on 14/4/12.
//  Copyright (c) 2014年 Momo. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <fstream>

#include <iomanip>

#include <vector>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems);
std::vector<std::string> split(const std::string &s, char delim);

int toInt(std::string input);
double toDouble(std::string input);

int getIntByLine();
std::string getStringByLine();
void dropLine();

double compute(float doneCost, float farmCost, float farmGenerate, float farmLevel) {
    float current_generate = 2.0 + farmGenerate * farmLevel;
    // compare
    float currentLevelSpendTime = doneCost / current_generate;
    float nextLevelSpendTime = farmCost / current_generate + doneCost / (current_generate + farmGenerate);
    if (currentLevelSpendTime <= nextLevelSpendTime)
        return currentLevelSpendTime;
    return farmCost / current_generate + compute(doneCost, farmCost, farmGenerate, farmLevel + 1);
}

void doCalcuate() {
    double farmCost;
    std::cin >> farmCost;
    double farmGenerate;
    std::cin >> farmGenerate;
    double doneCost;
    std::cin >> doneCost;
    std::cout << std::fixed << std::setprecision(7) <<compute(doneCost, farmCost, farmGenerate, 0);
}

int main(int argc, const char * argv[]) {
    std::ifstream in;
    std::ofstream out;
    if (argc >= 2) {
        // cin from file
        in.open(argv[1]);
        std::cin.rdbuf(in.rdbuf());
        // cout to file
        out.open("/Users/momo/Downloads/output");
        std::cout.rdbuf(out.rdbuf());
    }
    // read from cin
    else {
    }
    
    // test case pattern
    int number = getIntByLine();
    for (int i = 1; i <= number; i ++) {
        std::cout << "Case #" << i << ": " ;
        doCalcuate();
        std::cout << std::endl;
    }
    return 0;
}

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}

int getIntByLine() {
    int line;
    std::cin >> line;
    // ignore new line
    dropLine();
    return line;
}

std::string getStringByLine() {
    std::string line;
    getline(std::cin, line);
    return line;
}

void dropLine() {
    std::string ignore;
    getline(std::cin, ignore);
}

int toInt(std::string input) {
    int output;
    std::istringstream(input) >> output;
    return output;
}

double toDouble(std::string input) {
    double output;
    std::istringstream(input) >> output;
    return output;
}



