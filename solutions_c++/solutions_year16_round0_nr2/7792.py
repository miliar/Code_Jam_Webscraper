#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>

#include <string.h>

unsigned int get_min_steps(std::string &str) {
    unsigned int r = 0;

    if (str.empty()) {
        return r;
    }

    char currentState = str[0];

    const char* p = &str[1];

    while (*p != 0) {
        if (*p != currentState) {
            ++r;
            currentState = *p;
        }
        ++p;
    }

    r = currentState == '+' ? r : r+1;
    return r;
}

int main(int argc, char* argv[]) {
    std::ifstream inputFile;
    std::ofstream outputFile;

    if (argc > 1) {
        inputFile.open(argv[1]);
        outputFile.open(argv[1] + std::string(".out"));
    }
    else {
        inputFile.open("B-large.in");
        outputFile.open("B-large.in.out");
    }

    unsigned int T = 0;
    std::vector<std::string> cases;

    inputFile >> T;

    if (inputFile.good()) {
        std::string str;
        for (unsigned int i=0; i<T && !inputFile.eof(); ++i) {
            inputFile >> str;
            outputFile << "Case #" << i+1 << ": " << get_min_steps(str) << std::endl;
        }
    }

    inputFile.close();
    outputFile.close();
    return 0;
}
