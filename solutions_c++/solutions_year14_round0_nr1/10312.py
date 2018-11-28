#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>

const char* INPUT_FILE = "input.txt";
const char* OUTPUT_FILE = "output.txt";


typedef std::array<unsigned, 4> row;
typedef std::array<row, 4> cards;

int main(int argc, char *argv[])
{
    std::ifstream input{INPUT_FILE};
    std::ofstream output{OUTPUT_FILE};
    unsigned amountOfTestCases = 0; // the amount of test cases we need to perform

    // get the amount of test cases
    input >> amountOfTestCases;

    for (unsigned i = 0u; i < amountOfTestCases; ++i)
    {
        output << "Case #" << i+1 << ": ";

        unsigned cardRow[2];
        cards givenCards[2];
        row requiredRows[2];

        for (unsigned i = 0u; i < 2; ++i)
        {
            // get the data
            input >> cardRow[i];
            for(auto& r : givenCards[i])
            {
                for(auto& e : r) input >> e;
            }

            // retrieve the row the volenteer said
            for(unsigned k = 0; k < 4; ++k)
            {
                requiredRows[i][k] = givenCards[i][cardRow[i] - 1][k];
            }
            
            std::cout << "requiredRow[" << i << "]=";
            for(unsigned j = 0; j < 4; ++j)
            {
                std::cout << requiredRows[i][j] << ' ';
            }
            std::cout << '\n';
        }

        std::cout << "Looking for duplicates\n";

        // find the duplicates
        // in the required rows
        std::vector<unsigned> duplicates;
        for (unsigned j = 0u; j < 4; ++j)
        {
            auto e1 = requiredRows[0][j];
            for (unsigned i = 0u; i < 4; ++i)
            {
                auto e2 = requiredRows[1][i];
                // if we found a duplicate
                if(e1 == e2)
                {
                    // add it to the list
                    duplicates.push_back(e1);

                    std::cout << "Found duplicate: " << e1 << '\n';
                }
            }
        }

        // if we didn't find a duplicate
        if(duplicates.size() == 0)
        {
            output << "Volunteer cheated!"; // then the volenteer cheated
        }
        // otherwise if there is more than one duplicate
        else if(duplicates.size() > 1)
        {
            output << "Bad magician!";
        }
        else
        {
            output << duplicates[0];
        }
        output << '\n';
    }

    return 0;
}
