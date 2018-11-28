#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int T = 0, N = 0;
    char str[100][101];
    int nChar[100];
    int pos[100];
    int result;
    int average;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases)
    {
        // input
        cin >> N;
        for (int i = 0; i < N; ++i)
        {
            cin >> str[i];
            pos[i] = 0;
        }

        // process
        result = 0;
        while (str[0][pos[0]] != '\0')
        {
            average = 0;
            for (int i = 1; i < N; ++i)
            {
                if (str[i][pos[i]] != str[0][pos[0]])
                {
                    result = -1; // mark
                    break;
                }

                // count number of char
                for (nChar[i] = 0; str[i][pos[i]] == str[i][pos[i]+nChar[i]]; ++nChar[i]);
                pos[i] += nChar[i];
                average += nChar[i];
            }
            if (-1 == result)
                break;

            for (nChar[0] = 0; str[0][pos[0]] == str[0][pos[0]+nChar[0]]; ++nChar[0]);
            pos[0] += nChar[0];
            average += nChar[0];

            average = average / (float)N + 0.5;
            for (int i = 0; i < N; ++i)
            {
                result += abs(average - nChar[i]);
            }
        }

        // make sure every string reach the end
        for (int i = 1; i < N; ++ i)
        {
            if (str[i][pos[i]] != '\0')
            {
                result = -1;
                break;
            }
        }

        if (-1 == result)
            cout << "Case #" << cases << ": Fegla Won" << endl;
        else
            cout << "Case #" << cases << ": " << result << endl;
    }
    return 0;
}
