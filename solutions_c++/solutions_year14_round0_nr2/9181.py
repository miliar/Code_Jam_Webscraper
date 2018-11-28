#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char** argv)
{
    if (argc != 3)
    {
        cerr << "Invalid commandline parameters" << endl;
        return -1;
    }

    fstream input(argv[1], fstream::in);
    fstream output(argv[2], fstream::out | fstream::trunc);

    int numTestCases;
    input >> numTestCases;

    double C, F, X;
    double farmTime, answer, rateOfProduction, timeToAddFarm;
    const double standardProduction = 2.0;

    for (int i = 0; i < numTestCases; i++)
    {
        input >> C >> F >> X;

        rateOfProduction = standardProduction;
        farmTime = 0;
        answer = X / rateOfProduction;

        while (true)
        {
            farmTime += C / rateOfProduction;
            rateOfProduction += F;
            if (farmTime + X / rateOfProduction < answer)
            {
                answer = farmTime + X / rateOfProduction;
            }
            else
            {
                break;
            }
        }

        output << "Case #" << (i + 1) << ": " << setiosflags(ios::fixed) << setprecision(7) << answer << endl;
    }
}