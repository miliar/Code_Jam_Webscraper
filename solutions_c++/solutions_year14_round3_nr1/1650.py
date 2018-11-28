#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <vector>

struct TestCase
{
    size_t P;

    size_t Q;
};

std::vector<TestCase> ReadCases(std::istream& stream)
{
    char buffer[1000];

    int totalCases;
    std::vector<TestCase> result;

    stream >> totalCases;

    for (int i = 0; i < totalCases; i++)
    {
        TestCase testCase;

        stream >> testCase.P;

//        stream.getline(buffer, 1000, '/');
        stream.get();

//        std::istringstream strstream(buffer);

//        strstream >> testCase.P;
        stream >> testCase.Q;

        result.push_back(testCase);
    }

    return result;
}

size_t FindNearestFullElfAncestor(size_t p, size_t q)
{
    if (p * 2 >= q)
    {
        return 1;
    }
    else if (q > 2)
    {
        return FindNearestFullElfAncestor(p, q/2) + 1;
    }
    else
    {
        assert(false);
    }
}

std::pair<size_t, bool> Solve(size_t p, size_t q)
{
    if (q == 0)
    {
        return std::pair<size_t, bool>(0, false);
    }

    // Simplify.
    bool found = true;
    while (found)
    {
        found = false;
        for (size_t i = 2; i <= p; i++)
        {
            if ((p % i == 0) && (q % i == 0))
            {
                p /= i;
                q /= i;
                found = true;
                break;
            }
        }
    }

    // Check if q is a degree of 2
    size_t tq = q;
    for (size_t i = 0; i < 64; i++)
    {
        if (tq & 0x1)
        {
            tq >>= 1;

            break;
        }

        tq >>= 1;
    }

    for (size_t i = 0; i < 64; i++)
    {
        if (tq & 0x1)
        {
            return std::pair<size_t, bool>(0, false);
        }

        tq >>= 1;
    }

    return std::pair<size_t, bool>(FindNearestFullElfAncestor(p, q), true);
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
        std::cout << "Case #" << testNum << ": ";

        auto res = Solve(testCase.P, testCase.Q);

        if (res.second)
        {
            std::cout << res.first;
        }
        else
        {
            std::cout << "impossible";
        }

        std::cout << std::endl;

        testNum++;
    }

    return 0;
}

