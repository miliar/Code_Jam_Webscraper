#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <map>
#include <cctype>

std::string solve(std::vector<int> counts, int total)
{
    std::vector<double> ratios;
    ratios.resize(counts.size());

    std::string result = "";
    auto inDoor = 0;

    while (total > 0) {
        for (auto i = 0; i < counts.size(); i++) {
            ratios[i] = static_cast<double>(counts[i]) / total;
        }

        auto maxRatio = std::max_element(ratios.begin(), ratios.end());
        auto dist = std::distance(ratios.begin(), maxRatio);

        --counts[dist];
        --total;

        result += ('A' + dist);
        ++inDoor;
        if ((std::all_of(ratios.begin(), ratios.end(), [&](double i) { return (i == ratios[0]); }) && ratios[0] < 0.5)
            || inDoor == 2) {
            result += ' ';
            inDoor = 0;
        }
    }

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
        int numParties;
        inputFile >> numParties;

        std::vector<int> counts;
        counts.resize(numParties);

        auto sum = 0;

        auto i = 0;
        while (numParties-- > 0) {
            inputFile >> counts[i];
            sum += counts[i];
            ++i;
        }

        std::cout << "Case #" << caseId << ": ";
        std::cout << solve(counts, sum);
        std::cout << std::endl;
    }

    return 0;
}
