#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


// Read number
inline static void Algorithm(int N, int &LastNum)
{
    static const int MaxIteration = 100;
    
    if (N == 0)
    {
        LastNum = -1;
    }
    unsigned short Mask = 0;

    for (int Iteration = 1; Iteration <= MaxIteration; Iteration++)
    {
        int Number = N * Iteration;
        LastNum = Number;

        while (Number)
        {
            Mask |= 1 << (Number - (Number / 10) * 10);
            Number /= 10;
        }

        if (Mask == 1023)
        {
            break;
        }
    }
    if (Mask != 1023)
    {
        LastNum = -1;
    }
}

void main()
{
    int T;

    // Read case number.
    cin >> T;

    for ( int CaseId = 1; CaseId <= T; ++CaseId )
    {
        int N;
        int LastNum = -1;

        // Read inputs.
        cin >> N;

        // Algorithm
        Algorithm(N, LastNum);

        // Output.
        if (LastNum > 0)
        {
            cout << "Case #" << CaseId << ": " << LastNum << endl;
        }
        else
        {
            cout << "Case #" << CaseId << ": INSOMNIA" << endl;
        }
    }
}


 
