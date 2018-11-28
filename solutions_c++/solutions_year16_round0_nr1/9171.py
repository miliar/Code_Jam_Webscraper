#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

void flipDigits(int N, std::vector<bool>& digits)
{
    do {
        digits[N % 10] = true;
        N /= 10;
    } while(N > 0);   
}

int solve(int N)
{
    if (N == 0) {
        return 0;
    }

    std::vector<bool> seenDigits = {false,false,false,false,false,false,false,false,false,false};

    auto N_ = N;
    int i = 1;
    do {
        N_ = N * i++;
        flipDigits(N_, seenDigits);
    }
    while (! std::all_of(seenDigits.begin(), seenDigits.end(), [](bool b) {return b;}));

    return N_;
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
        int N;
        inputFile >> N;

        std::cout << "Case #" << caseId << ": ";

        auto solution = solve(N);
        if (solution > 0) {
            std::cout << solution;
        }
        else {
            std::cout << "INSOMNIA";
        }

        std::cout << std::endl;
    }

    return 0;
}
