#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

static const uint64_t N = 16;
static const uint64_t J = 500;

inline static uint64_t GetInterpretation(uint64_t Number, uint64_t Base)
{
    uint64_t ResidualNumber;
    uint64_t Iteration;
    uint64_t Interpretation;

    ResidualNumber = Number;
    Iteration = 0;
    Interpretation = 0;
    while (ResidualNumber)
    {
        if (ResidualNumber % 2 == 1)
        {
            Interpretation += _Pow_int(Base, Iteration);
        }
        ResidualNumber = ResidualNumber / 2;
        Iteration++;
    }

    return Interpretation;
}

inline static uint64_t FindDivisor(uint64_t Number)
{
    uint64_t Divisor;
    uint64_t DivisorMax = sqrtl(Number);
    uint64_t Flag = 0;

    for (Divisor = 2; Divisor <= DivisorMax; Divisor++)
    {
        if (Number%Divisor == 0)
        {
            Flag = 1;
            break;
        }
    }

    if (Flag != 1)
    {
        Divisor = 0;
    }
    return Divisor;
}

// Read number
inline static void Algorithm(uint64_t(&Jamcoin)[J], uint64_t(&Divisor)[J][9])
{
    static const uint64_t JamcoinMin = _Pow_int(2, N - 1) + 1;
    static const uint64_t JamcoinMax = _Pow_int(2, N + 1) - 1;
    uint64_t ResultCnt = 0;

    for (uint64_t TestedValue = JamcoinMin; TestedValue <= JamcoinMax; TestedValue += 2)
    {
        uint64_t Flag = 1;

        // Get interpretation.
        uint64_t TempDevisor[9];
        for (uint64_t Base = 2; Base <= 10; ++Base)
        {
            uint64_t Interpretation = GetInterpretation(TestedValue, Base);
            TempDevisor[Base - 2] = FindDivisor(Interpretation);
            if (TempDevisor[Base - 2] == 0)
            {
                Flag = 0;
                break;
            }
        }
        if (Flag == 1)
        {
            Jamcoin[ResultCnt] = TestedValue;
            for (int Temp = 0; Temp < 9; ++Temp)
            {
                Divisor[ResultCnt][Temp] = TempDevisor[Temp];
            }
            ResultCnt++;
            if (ResultCnt >= J)
            {
                break;
            }
        }
    }
}

void main()
{
    uint64_t Jamcoin[J];
    uint64_t Divisor[J][9];

    // Init
    for (int Temp = 0; Temp < J; ++Temp)
    {
        Jamcoin[Temp] = 0;
        for (int Temp2 = 0; Temp2 < 9; ++Temp2)
        {
            Divisor[Temp][Temp2] = 0;
        }
    }

    // Algorithm
    Algorithm(Jamcoin, Divisor);

    // Output.
    cout << "Case #" << 1 << ":" << endl;
    for (uint64_t JamcoinId = 0; JamcoinId < J; ++JamcoinId)
    {
        uint64_t JamcoinResidual = Jamcoin[JamcoinId];
        uint64_t JamcoinDigit[N];
        uint64_t Iteration = 0;
        for (Iteration = 0; Iteration < N; Iteration++)
        {
            JamcoinDigit[N - Iteration - 1] = JamcoinResidual % 2;
            JamcoinResidual /= 2;
        }
        for (uint64_t Temp = 0; Temp < N; ++Temp)
        {
            cout << JamcoinDigit[Temp];
        }
        for (uint64_t Temp = 0; Temp < N; ++Temp)
        {
            cout << JamcoinDigit[Temp];
        }

        for (uint64_t Temp = 0; Temp < 9; ++Temp)
        {
            cout << " " << Divisor[JamcoinId][Temp];
        }
        cout << endl;
    }
}

