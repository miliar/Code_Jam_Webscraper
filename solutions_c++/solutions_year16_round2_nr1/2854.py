/*
 * Header file available here:
 * https://github.com/JosephConrad/GoogleCodeJam/tree/master/2016
 */
#include "../../template.h"



void processNumber(char let, std::string alpha, int result[10], int num, std::map<char, int>& lettersCounter) {
    if (lettersCounter[let] > 0) {
        int number = lettersCounter[let];
        result[num] = number;
        for(auto& c : alpha) {
            lettersCounter[c] = lettersCounter[c]-number;
        }
    }
}


std::string solve(std::vector<char> letters) {
    int changes = 0;

    int result[10];
    for (int i = 0; i < 10; ++i) {
        result[i] = 0;
    }

    std::map<char, int> lettersCounter;

    char previous = letters[0];
    for (auto &letter: letters) {
        lettersCounter[letter] = lettersCounter[letter] + 1;
    }

    char let = 'Z';
    std::string alpha = "ZERO";
    int num = 0;
    processNumber(let, alpha, result,num,
                  lettersCounter);
    let = 'W';
    alpha = "TWO";
    num = 2;
    processNumber(let, alpha, result, num,
                  lettersCounter);

    let = 'U';
    alpha = "FOUR";
    num = 4;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'X';
    alpha = "SIX";
    num = 6;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'G';
    alpha = "EIGHT";
    num = 8;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'O';
    alpha = "ONE";
    num = 1;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'H';
    alpha = "THREE";
    num = 3;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'F';
    alpha = "FIVE";
    num = 5;
    processNumber(let, alpha, result,num,
                  lettersCounter);

    let = 'S';
    alpha = "SEVEN";
    num = 7;
    processNumber(let, alpha, result,num,
                  lettersCounter);
    result[9] = lettersCounter['N']/2;

    std::string print = "";
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < result[i]; ++j)
        print += std::to_string(i);
    }
    return print;
}


int main() {

#ifndef GOOGLE_CODE_JAM
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    clock_t start = clock();

    std::string name;
    std::getline(std::cin, name);
    int T = std::stoi(name);
    REP(cc, T) {
        std::getline(std::cin, name);
        std::vector<char> letters = splitString<char, std::vector>(name);
        printf("Case #%d: %s\n", cc + 1, solve(letters).c_str());
    }
    fprintf(stderr, "*** Total time: %.3lf seconds ***\n",
            ((clock() - start) / (double) CLOCKS_PER_SEC));
    return 0;
}
