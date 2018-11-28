#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>

struct Arrangement
{
    int cards[4][4];
};

struct TestCase
{
    Arrangement arrangement1;

    Arrangement arrangement2;

    int firstChoice;

    int secondChoice;
};

void ReadArrangement(std::istream& stream, Arrangement& a)
{
    for (int r = 0; r < 4; r++)
    {
        for (int c = 0; c < 4; c++)
        {
            stream >> a.cards[r][c];
        }
    }
}

std::vector<TestCase> ReadCases(std::istream& stream)
{
    int totalCases;
    std::vector<TestCase> result;

    stream >> totalCases;

    for (int i = 0; i < totalCases; i++)
    {
        TestCase testCase;

        stream >> testCase.firstChoice;

        ReadArrangement(stream, testCase.arrangement1);

        stream >> testCase.secondChoice;

        ReadArrangement(stream, testCase.arrangement2);

        result.push_back(testCase);
    }

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
        std::set<int> firstSet =
        {
            testCase.arrangement1.cards[testCase.firstChoice - 1][0],
            testCase.arrangement1.cards[testCase.firstChoice - 1][1],
            testCase.arrangement1.cards[testCase.firstChoice - 1][2],
            testCase.arrangement1.cards[testCase.firstChoice - 1][3]
        };

        std::set<int> secondSet =
        {
            testCase.arrangement2.cards[testCase.secondChoice - 1][0],
            testCase.arrangement2.cards[testCase.secondChoice - 1][1],
            testCase.arrangement2.cards[testCase.secondChoice - 1][2],
            testCase.arrangement2.cards[testCase.secondChoice - 1][3]
        };

        std::vector<int> result;

        std::set_intersection(
            firstSet.begin(),
            firstSet.end(),
            secondSet.begin(),
            secondSet.end(),
            std::insert_iterator< std::vector<int> >( result, result.begin()));

        std::cout << "Case #" << testNum << ": ";

        if (result.size() == 1)
        {
            std::cout << result[0];
        }
        else if (result.size() == 0)
        {
            std::cout << "Volunteer cheated!";
        }
        else
        {
            std::cout << "Bad magician!";
        }

        std::cout << std::endl;

        testNum++;
    }

    return 0;
}

