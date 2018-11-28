#include <string>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>

void flip(std::vector<bool>& state, uint32_t index)
{
    std::reverse(state.begin(), state.begin() + index + 1);
    for (uint32_t i = 0; i <= index; ++i)
        state[i] = !state[i];
}

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
    inputFile.ignore(100, '\n');

    for (uint16_t t = 1; t <= numTestCases; ++t)
    {
        std::string initial_state;
        std::getline(inputFile, initial_state, '\n');
        std::vector<bool> state(initial_state.size(), false);
        std::transform(initial_state.begin(), initial_state.end(), state.begin(), [](const char& c) { return c == '+'; });

        uint32_t numFlips = 0;
        for (int32_t i = state.size() - 1; i >= 0; --i)
        {
            if (!state[i] && !state[0])
            {
                flip(state, i);
                numFlips++;
            }
            else if (!state[i])
            {
                int32_t j;
                for (j = i; j >= 0; --j)
                {
                    if (state[j])
                        break;
                }

                if (j > -1)
                {
                    flip(state, j); 
                    numFlips++;
                }
                    
                flip(state, i); 
                numFlips++;
            }
        }

        outFile << "Case #" << t << ": " << numFlips << std::endl;
    }        
}