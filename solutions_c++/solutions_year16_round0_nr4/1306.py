#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

static const uint64_t KMax = 100;

inline static uint64_t CalcStartPos(uint64_t K, uint64_t C)
{
    uint64_t Pos = 0;
    uint64_t NestLvl = C - 1;
    uint64_t Iteration = 1;
    while (NestLvl >= 1)
    {
        uint64_t LvlTotalLen = _Pow_int(K, NestLvl);
        Pos += Iteration * LvlTotalLen / K;
        NestLvl--;
        Iteration++;
    }
    Pos += 1;

    return Pos;
}
inline static void Algorithm(uint64_t K, uint64_t C, uint64_t S, uint64_t &ResultLen, uint64_t (&Result)[KMax])
{
    if (C + S > K)
    {
        if (C < K)
        {
            ResultLen = K - C + 1;
        }
        else
        {
            C = K;
            ResultLen = 1;
        }
        // Find position
        uint64_t StartPos = CalcStartPos(K, C);
        for (uint64_t Temp = 0; Temp < ResultLen; ++Temp)
        {
            Result[Temp] = StartPos + Temp;
        }
        
    }
    else
    {
        ResultLen = 0;
    }
}

void main()
{
    uint64_t T;

    // Read case number.
    cin >> T;

    for (uint64_t CaseId = 1; CaseId <= T; ++CaseId)
    {
        uint64_t K, C, S;
        uint64_t ResultLen, Result[KMax];

        // Read inputs.
        cin >> K >> C >> S;

        // Algorithm
        Algorithm(K, C, S, ResultLen, Result);

        // Output.
        cout << "Case #" << CaseId << ":";
        if (ResultLen == 0)
        {
            cout << " IMPOSSIBLE" << endl;
        }
        else
        {
            for (uint64_t Temp = 0; Temp < ResultLen; ++Temp)
            {
                cout << " " << Result[Temp];
            }
            cout << endl;
        }
    }
}
