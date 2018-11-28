#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cctype>

std::string solve(const std::string& s)
{
    std::map<char, int32_t> countChars;
    std::vector<char> digits;

    for (auto& c : s) {
        ++countChars[std::tolower(c)];
    }

    auto i = 0;
    while (i < s.length()) {
        if (countChars['z'] > 0) {
            --countChars['z'];
            --countChars['e'];
            --countChars['r'];
            --countChars['o'];

            i += 4;
            digits.push_back('0');
            continue;
        }
        if (countChars['w'] > 0) {
            --countChars['t'];
            --countChars['w'];
            --countChars['o'];

            i += 3;
            digits.push_back('2');
            continue;
        }
        if (countChars['u'] > 0) {
            --countChars['f'];
            --countChars['o'];
            --countChars['u'];
            --countChars['r'];

            i += 4;
            digits.push_back('4');
            continue;
        }
        if (countChars['f'] > 0) {
            --countChars['f'];
            --countChars['i'];
            --countChars['v'];
            --countChars['e'];

            i += 4;
            digits.push_back('5');
            continue;
        }
        if (countChars['r'] > 0) {
            --countChars['t'];
            --countChars['h'];
            --countChars['r'];
            --countChars['e'];
            --countChars['e'];

            i += 5;
            digits.push_back('3');
            continue;
        }
        if (countChars['x'] > 0) {
            --countChars['s'];
            --countChars['i'];
            --countChars['x'];

            i += 3;
            digits.push_back('6');
            continue;
        }
        if (countChars['g'] > 0) {
            --countChars['e'];
            --countChars['i'];
            --countChars['g'];
            --countChars['h'];
            --countChars['t'];

            i += 5;
            digits.push_back('8');
            continue;
        }
        if (countChars['v'] > 0) {
            --countChars['s'];
            --countChars['e'];
            --countChars['v'];
            --countChars['e'];
            --countChars['n'];

            i += 5;
            digits.push_back('7');
            continue;
        }
        if (countChars['i'] > 0) {
            --countChars['n'];
            --countChars['i'];
            --countChars['n'];
            --countChars['e'];

            i += 4;
            digits.push_back('9');
            continue;
        }
        if (countChars['o'] > 0) {
            --countChars['o'];
            --countChars['n'];
            --countChars['e'];

            i += 3;
            digits.push_back('1');
            continue;
        }
    }

    std::sort(digits.begin(), digits.end());
    std::string result(digits.begin(), digits.end());
    return result;
}

int main(int argc, char** argv)
{
    if (argc < 2) {
        std::cout << "Not enough arguments: " << argv[0] << " <input file>"
                  << std::endl;
    }

    std::ifstream inputFile(argv[1]);
    int numCases;

    inputFile >> numCases;

    int caseId = 0;
    while (++caseId <= numCases) {
        std::string s;
        inputFile >> s;

        std::cout << "Case #" << caseId << ": ";

        auto solution = solve(s);
        std::cout << solution;

        std::cout << std::endl;
    }

    return 0;
}
