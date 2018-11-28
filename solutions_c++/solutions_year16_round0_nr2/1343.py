#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

// Read string
inline static void Algorithm(string &Input, uint64_t &Number)
{
    uint64_t L = Input.length();
    char PreChar = Input[0];
    char CurChar;

    Number = 0;
    for (uint64_t Temp = 0; Temp < L; Temp++)
    {
        CurChar = Input[Temp];
        if (CurChar != PreChar)
        {
            Number++;
            PreChar = CurChar;
        }
    }
    if (CurChar == '-')
    {
        Number++;
    }
}

void main()
{
    uint64_t T;
    string InputLine;
    uint64_t Number;

    // Read case number.
    cin >> T;

    // Skip first line.
    getline(cin, InputLine);

    // Read input.
    for (int CaseId = 1; CaseId <= T; ++CaseId)
    {
        // Read inputs.
        getline(cin, InputLine);

        // Algorithm
        Algorithm(InputLine, Number);

        // Output.
        cout << "Case #" << CaseId << ": " << Number << endl;
    }
}
