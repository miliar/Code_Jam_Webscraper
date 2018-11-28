#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using std::cout;
using std::endl;
using std::string;

bool CheckAllPlus(std::vector<int>& cakes)
{
    bool result = true;

    // If it exists
    if (std::find(cakes.begin(), cakes.end(), 0) != cakes.end())
    {
        result = false;
    }

    return result;
}

size_t FindFlipIndex(std::vector<int>& cakes)
{
    size_t index = cakes.size() - 1;
    int first = cakes[0];
    
    for (size_t i = 0; i < cakes.size(); i++)
    {
        if (cakes[i] != first)
        {
            // Return 1 index previous
            index = i - 1;
            break;
        }
    }

    return index;
}

void Flip(std::vector<int>& cakes, size_t index)
{
    std::vector<int> tempVector;

    for (size_t i = 0; i <= index; i++)
    {
        tempVector.push_back(1 - cakes[i]);
    }

    for (size_t i = 0; i <= index; i++)
    {
        cakes[index - i] = tempVector[i];
    }
}

long Calculate(std::vector<int>& cakes)
{
    long tries = 0;

    while(!CheckAllPlus(cakes))
    {
        // Apply first flip
        size_t flipIndex = FindFlipIndex(cakes);
        Flip(cakes, flipIndex);

        tries++;
    }

    return tries;
}

int main()
{
    cout << "Working..." << endl;

    std::ifstream input("input.txt" );
    std::ofstream output("output.txt");
    string line;
    std::getline(input, line);
    std::istringstream ss(line);

    int caseCount = 0;
    ss >> caseCount;

    for (int i = 0; i < caseCount; i++)
    {
        std::getline(input, line);
        std::vector<int> cakes;

        for (size_t i = 0; i < line.length(); i++)
        {
            cakes.push_back(line[i] == '+' ? 1 : 0);
        }

        int result = Calculate(cakes);

        output << "Case #" << (i + 1) << ": " << result << endl;
    }

    input.close();
    output.close();

    cout << "Done!" << endl;

    return 0;
}
