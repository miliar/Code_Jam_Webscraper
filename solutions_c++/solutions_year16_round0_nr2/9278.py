#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

void flipRange(std::vector<char>::iterator l, std::vector<char>::iterator r)
{
    std::transform(l, r, l, [](char c) { return c == '-' ? '+' : '-'; });
    std::reverse(l, r);
}

int solve(std::vector<char>&& input)
{
    int flips = 0;
    while (std::any_of(input.begin(), input.end(), [](char c) { return c == '-'; })) {
        auto top = input.begin();
        auto bottom = std::mismatch(top, input.end(), top + 1);

        flipRange(top, bottom.second);
        flips++;
    }

    return flips;
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
    // Skip the newline.
    inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    int caseId = 0;
    while (++caseId <= numCases) {
        std::string S;
        std::getline(inputFile, S);

        std::cout << "Case #" << caseId << ": "
                  << solve(std::vector<char>(S.begin(), S.end())) << std::endl;
    }

    return 0;
}
