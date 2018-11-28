/*
 * StandingOvation.h
 *
 *  Created on: Apr 11, 2015
 *      Author: gustavo
 */

#ifndef STANDINGOVATION_H_
#define STANDINGOVATION_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <assert.h>
#include <fstream>
#include <utility>
#include <iostream>
#include <stdexcept>

#include <vector>
#include <algorithm>


class StandingOvation {
public:
    void main(std::string filePath, std::string outPath) {
        std::ifstream in;
        in.open(filePath.c_str());
        if (!in) throw std::runtime_error("Problem with file");
        std::cout << "\nProcessing " << filePath << "\n";
        std::ofstream out;
        out.open(outPath.c_str());

        std::string line;
        getline(in, line);
        int testCases = atoi(line.c_str());
//        std::cout << testCases << " test cases \n";
        for (int testCase = 0; testCase < testCases; ++testCase) {
            char c;
            int SMax = 0;
            in.get(c);
            while (c != ' ') {
//                std::cout << c << " c \n";
                SMax *= 10;
                SMax += c - '0';
                in.get(c);
//                std::cout << SMax << " SMax \n";
            }

            std::vector<int> aud(SMax + 1);
            for (int i = 0; i <= SMax; ++i) {
                in.get(c);
                aud[i] = c - '0';
            }

            int needed = 0;
            int curCount = 0;
            for (int i = 0; i <= SMax; ++i) {
                if (aud[i] == 0) continue;
                if (curCount < i) {
                    needed += i - curCount;
                    curCount = i;
                }
                curCount += aud[i];
            }
            std::cout << "Case #" << testCase + 1 << ": " << needed << "\n";
            out << "Case #" << testCase + 1 << ": " << needed << "\n";
            getline(in, line);
        }

    }

};

#endif /* STANDINGOVATION_H_ */
