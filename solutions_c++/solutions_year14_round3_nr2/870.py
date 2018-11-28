#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>

struct TestCase
{
    std::vector<std::string> trains;
};

std::string SimplifyString(const std::string& str)
{
    std::string result;

    int prev = -1;

    for (auto c : str)
    {
        if (c != prev)
        {
            result.push_back(c);
        }

        prev = c;
    }

    return result;
}

std::vector<TestCase> ReadCases(std::istream& stream)
{
    char buffer[1000];
    int totalCases;
    std::vector<TestCase> result;

    stream >> totalCases;

    for (int i = 0; i < totalCases; i++)
    {
        TestCase testCase;

        size_t trainNum;

        stream >> trainNum;

        for (size_t j = 0; j < trainNum; j++)
        {
            std::string str;
            stream >> str;

//            stream.getline(buffer, 1000);
            testCase.trains.push_back(SimplifyString(str));
        }

        result.push_back(testCase);
    }

    return result;
}

bool CheckTrain(std::vector<std::string>& trains)
{
    std::set<int> visited;

    int prev = -1;
    for (auto& str: trains)
    {
        for (auto c : str)
        {
            // New letter
            if ((prev >= 0) && (prev != c))
            {
                if (visited.count(prev) > 0)
                {
                    return false;
                }

                visited.insert(prev);
            }

            prev = c;
        }
    }

    if (visited.count(prev) > 0)
    {
        return false;
    }

    return true;
}

size_t Solve(const TestCase& testCase)
{
    size_t result = 0;

    // Create index vector;
    std::vector<size_t> indices;
    for (size_t i = 0; i < testCase.trains.size(); i++)
    {
        indices.push_back(i);
    }

    do
    {
        std::vector<std::string> trains;

        for (auto i : indices)
        {
            trains.push_back(testCase.trains[i]);
        }

        if (CheckTrain(trains))
        {
            result++;
        }
    }
    while (std::next_permutation(indices.begin(), indices.end()));


    return result;
}

int main(int argc, char* argv[])
{
    std::vector<TestCase> cases;

    if (argc == 1)
    {
        cases = ReadCases(std::cin);
    }
    else if (argc == 2)
    {
        std::ifstream stream(argv[1]);
        if (!stream.good())
        {
            return 1;
        }

        cases = ReadCases(stream);
    }
    else
    {
        return 1;
    }

    int testNum = 1;
    for (auto& testCase : cases)
    {
        std::cout << "Case #" << testNum << ": " << Solve(testCase);

        std::cout << std::endl;

        testNum++;
    }

    return 0;
}

