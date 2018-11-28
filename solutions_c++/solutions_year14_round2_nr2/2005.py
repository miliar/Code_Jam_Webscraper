#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <windows.h>

using namespace std;

void main()
{
    int T = 0;
    int startTime = 0;

    ifstream in("B-small-attempt0.in");
    ofstream out("B-small-attempt0.out");

    in >> T;

    for(int i=0; i<T; ++i)
    {
        startTime = GetTickCount();

        int A, B, K;

        in >> A >> B >> K;

        int solve = 0;

        for(int i=0; i< A; i++)
        {
            for(int j=0; j<B; j++)
            {
                int r = i&j;
                if(r < K)
                    solve++;
            }
        }

        out << "Case #" << i+1 << ": " << solve;

        out << endl;


        cout << "Case #" << i+1 << ", time(ms) =  " << GetTickCount() - startTime << endl;
    }
}