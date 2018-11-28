#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int main ()
{
    int T;
    int caseCount = 0;
    cin >> T;
    while ( T-- )
    {
        caseCount++;

        int N, M;
        cin >> N >> M;
        int pattern[105][105];
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                cin >> pattern[i][j];
        
        int rowCut[105];
        int colCut[105];
        int H;
        // Rows
        for (int i = 0; i < N; ++i)
        {
            H = 1;
            for (int j = 0; j < M; ++j)
            {
                H = max(H, pattern[i][j]);
            }
            rowCut[i] = H;
        }
        // Cols
        for (int j = 0; j < M; ++j)
        {
            H = 1;
            for (int i = 0; i < N; ++i)
            {
                H = max(H, pattern[i][j]);
            }
            colCut[j] = H;
        }
        bool isPossible = true;
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                if (pattern[i][j] < min(rowCut[i], colCut[j]))
                {
                    isPossible = false;
                    break;
                }

            }
            if (! isPossible)
                break;
        }
        cout << "Case #"
             << caseCount
             << ": ";
        if (isPossible)
            cout << "YES";
        else
            cout << "NO";
        cout << endl;
        
    }
    return 0;
}