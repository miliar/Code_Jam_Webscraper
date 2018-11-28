//
//  main.cpp
//  Magic Trick
//
//  Created by Momo on 14/4/12.
//  Copyright (c) 2014年 Momo. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <fstream>


#include <vector>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems);
std::vector<std::string> split(const std::string &s, char delim);

int toInt(std::string input);

int getIntByLine();
std::string getStringByLine();
void dropLine();

void doCalcuate() {
    // get first
    bool cards[2][17] = {false};
    for (int i = 0; i < 2; i ++) {
        int row = getIntByLine();
        for (int j = 1; j <= 4; j ++) {
            if (j == row) {
                std::vector<std::string> tokens = split(getStringByLine(), ' ');
                for (auto itr = tokens.begin(); itr != tokens.end(); itr ++) {
                    cards[i][toInt(*itr)] = true;
                }
            }
            else {
                dropLine();
            }
        }
    }
    
    // check compare
    std::vector<int> compare_card_list;
    for (int i = 1; i <= 16; i ++) {
        if (cards[0][i] == false)
            continue ;
        if (cards[1][i] == false)
            continue ;
        if (cards[0][i] == cards[1][i]) {
            compare_card_list.push_back(i);
        }
    }
    
    // output
    if (compare_card_list.size() == 1) {
        std::cout << compare_card_list.at(0);
    }
    else if (compare_card_list.size() == 0) {
        std::cout << "Volunteer cheated!";
    }
    else {
        std::cout << "Bad magician!";
    }
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
