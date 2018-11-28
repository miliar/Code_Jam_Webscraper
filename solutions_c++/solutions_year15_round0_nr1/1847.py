enum Contest { CodeChef, CodeJam };
enum IOBinding { File, StandartStream };

Contest contest = CodeJam;

IOBinding inputBinding = File;
//IOBinding inputBinding = StandartStream;

IOBinding outputBinding = File;
//IOBinding outputBinding = StandartStream;

#include <string>
#include <fstream>
#include <istream>
#include <ostream>
#include <iostream>

std::istream *input;
std::ostream *output;

void solveCase() {
    char *str;
    int sMax, res = 0, standing = 0;
    *input >> sMax;

    str = new char [sMax + 2];
    *input >> str;

    standing = str[0] - '0';
    for(int i = 1; i <= sMax; ++i) {
        if (standing < i) {
            res += i - standing;
            standing = i;
        }
        standing += str[i] - '0';
    }

    delete[] str;

    *output << res << '\n';
}

int main(int argc, char *argv[])
{
    std::ios_base::sync_with_stdio(false);

    if (inputBinding == File)
        input = new std::ifstream("input.txt");
    else input = &std::cin;

    if (outputBinding == File)
        output = new std::ofstream("output.txt");
    else output = &std::cout;

    int T; *input >> T;
    for(int t = 1; t <= T; ++t) {
        if (contest == CodeJam)
            *output << "Case #" << t << ": ";
        solveCase();
    }

    if (inputBinding == File) delete input;
    if (outputBinding == File) delete output;

    return 0;
}
