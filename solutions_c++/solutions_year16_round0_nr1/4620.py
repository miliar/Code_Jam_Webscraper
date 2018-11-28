#include <bitset>
#include <string>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <algorithm>

int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        std::cerr << "Usage: " << argv[0] << " <test_file> <output_file>" << std::endl;
        return 1;
    }

    auto inputFilename = argv[1];
    std::ifstream inputFile(inputFilename);
    if (!inputFile.is_open())
    {
        std::cerr << "File not found: '" << inputFilename << "'" << std::endl;
        return 2;
    }

    auto outputFilename = argv[2];
    std::ofstream outFile(outputFilename);
    if (!outFile.is_open())
    {
        std::cerr << "Could not open file '" << outputFilename << "' for writing." << std::endl;
        return 2;
    }

    uint16_t numTestCases;
    inputFile >> numTestCases;

    for (uint16_t i = 1; i <= numTestCases; ++i)
    {
        uint64_t n, n_times_m;
        inputFile >> n;

        std::bitset<10> numbers_seen(0);
        if (n != 0)
        {
            for (uint32_t m = 1; !numbers_seen.all(); ++m)
            {
                n_times_m = n * m;
                auto number = std::to_string(n_times_m);
                for (const auto& c: number)
                {
                    numbers_seen[c - '0'] = true;
                }
            }
        }

        outFile << "Case #" << i << ": ";
        if (numbers_seen.all())
            outFile << n_times_m;
        else
            outFile << "INSOMNIA";
        outFile << std::endl;
    }
        
}