#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

static const double INITIAL_COOKIES_PER_SECOND = 2.0;

struct TestCase
{
    double factoryPrice;

    double winAmount;

    double factoryRate;
};

struct State
{
    double cookies;

    double cookiesPerSecond;

    double time;
};

std::vector<TestCase> ReadCases(std::istream& stream)
{
    int totalCases;
    std::vector<TestCase> result;

    stream >> totalCases;

    for (int i = 0; i < totalCases; i++)
    {
        TestCase testCase;

        stream >> testCase.factoryPrice >> testCase.factoryRate >> testCase.winAmount;

        result.push_back(testCase);
    }

    return result;
}

double Calculate(double C, double X, double F)
{
    double pureWaitTime = X / INITIAL_COOKIES_PER_SECOND;

    double bestTime = pureWaitTime;

    double currentTime = 0.0;
    double currentSpeed = INITIAL_COOKIES_PER_SECOND;

    while (true)
    {
        // Wait until we can buy factory.
        currentTime += C / currentSpeed;
        currentSpeed += F;

        if (currentTime >= bestTime)
        {
            break;
        }

        double timeUntilWin = X / currentSpeed;
        if (currentTime + timeUntilWin < bestTime)
        {
            bestTime = currentTime + timeUntilWin;
        }
    }

    return bestTime;
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

    for (int i = 0; i < cases.size(); i++)
    {
        double winTime = Calculate(cases[i].factoryPrice, cases[i].winAmount, cases[i].factoryRate);
        std::cout << "Case #" << (i + 1) << ": " << std::fixed << std::setprecision(10) << winTime << std::endl;
    }
}

