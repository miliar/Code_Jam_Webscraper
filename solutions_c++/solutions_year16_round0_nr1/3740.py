// CodeJam2016-2.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <string>
#include <bitset>

int sheep(int N)
{
    std::bitset<10> digitsSeen;

    long long current = N;

    auto setBits = [&](long long current)
    {
        while (current >= 10)
        {
            digitsSeen.set(current % 10);
            current /= 10;
        }
        digitsSeen.set(current);
    };

    int i = 1;
    setBits(N * i);
    while (!digitsSeen.all())
    {
        setBits(N * ++i);
    }

    return N * i;
}

int main()
{
    std::ifstream input("1.in");

    int cases = 0;
    input >> cases;

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        int N;
        input >> N;

        if (N == 0)
        {
            printf("Case #%d: INSOMNIA\n", caseNumber + 1);
        }
        else
        {
            printf("Case #%d: %d\n", caseNumber + 1, sheep(N));
        }
    }

    getchar();

    return 0;
}

