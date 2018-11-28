#include <vector>
#include <cassert>
#include <algorithm>

#include <fstream>
#include <iostream>
#include <string>

std::vector<int> solveInstance(int K, int C, int S) {
    assert(K == S);

    std::vector<int> result(S);

    int i = 0;

    std::generate(result.begin(), result.end(), [&i]() { return ++i; });

    return result;
}

void printSolution(std::vector<int> const& solution) {
    for(auto d : solution) {
        std::cout << ' ' << d;
    }
}

int main(int argc, char** argv) {
    std::ifstream stream(argv[1]);

    std::string line;

    std::getline(stream,line);


    int T = atoi(line.c_str());

    for(int i = 0; i < T; ++i) {
        std::getline(stream, line);
        char* line_d = _strdup(line.c_str());
        char* line_p = line_d;

        int K = strtol(line_p, &line_p, 0);
        int C = strtol(line_p, &line_p, 0);
        int S = strtol(line_p, &line_p, 0);

        auto result = solveInstance(K, C, S);

        std::cout << "Case #" << i + 1 << ":";

        printSolution(result);

        std::cout << std::endl;

        free(line_d);
    }

    return 0;
}