//
//  main.cpp
//  Deceitful War
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
double toDouble(std::string input);

int getIntByLine();
std::string getStringByLine();
void dropLine();

int getDeceitfulWarCount(std::vector<double> naomi_blockes, std::vector<double> ken_blockes, int number) {
    int count = 0;
    for (auto ken_itr = ken_blockes.begin(); ken_itr != ken_blockes.end(); ken_itr ++) {
        bool haveChecked = false;
        for (auto naomi_itr = naomi_blockes.begin(); naomi_itr != naomi_blockes.end();) {
            if (*naomi_itr > *ken_itr) {
                naomi_itr = naomi_blockes.erase(naomi_itr);
                count ++;
                haveChecked = true;
                break ;
            }
            else {
                naomi_itr ++;
            }
        }
        if (haveChecked == false) {
            naomi_blockes.erase(naomi_blockes.begin());
        }
    }
    return count;
}

int getWarCount(std::vector<double> naomiBlocked, std::vector<double> kenBlockes, int number) {
    int count = 0;
    for (auto naomi_itr = naomiBlocked.begin(); naomi_itr != naomiBlocked.end(); naomi_itr ++) {
        bool haveChecked = false;
        for (auto ken_itr = kenBlockes.begin(); ken_itr != kenBlockes.end();) {
            if (*ken_itr > *naomi_itr) {
                ken_itr = kenBlockes.erase(ken_itr);
                count ++;
                haveChecked = true;
                break ;
            }
            else {
                ken_itr ++;
            }
        }
        // all of the blockes in ken are smaller than naomi, remove first one
        if (haveChecked == false) {
            kenBlockes.erase(kenBlockes.begin());
        }
    }
    return  number - count;
}

void doCalcuate() {
    int number = getIntByLine();
    std::vector<double> blockes[2];
    for (int i = 0; i < 2; i ++) {
        for (int j = 0; j < number; j ++) {
            std::string input;
            std::cin >> input;
            double data = toDouble(input);
            bool doInsert = false;
            auto itr = blockes[i].begin();
            for (; itr != blockes[i].end(); itr ++) {
                if (*itr > data) {
                    doInsert = true;
                    break ;
                }
            }
            if (doInsert) {
                blockes[i].insert(itr, data);
            }
            else {
                blockes[i].push_back(data);
            }
        }
    }
    std::cout << getDeceitfulWarCount(blockes[0], blockes[1], number) << " " << getWarCount(blockes[0], blockes[1], number);
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

