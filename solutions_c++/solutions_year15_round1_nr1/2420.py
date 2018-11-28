// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;
#define max(x,y) (x<y?y:x)
#define min(x,y) (x>y?y:x)

int _tmain(int argc, _TCHAR* argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;

        int y = 0;
        int rate = 0; // rate per 10 minutes for z
        int last;

        if (N > 0)
            cin >> last;
        vector<int> num;
        num.push_back(last);
        for (int j = 1; j < N; ++j)
        {
            int mj;
            cin >> mj;

            if (last > mj)
            {
                // some were eaten
                rate = max(rate, last - mj);
                y += (last - mj);
            }

            num.push_back(mj);
            last = mj;
        }

        int z = 0;
        for (int j = 0; j < N-1; ++j)
        {
            // from this time to the next we lost rate
            z += min(rate, num[j]);
        }

        cout << "Case #" << (1 + i) << ": " << y << " " << z << endl;
    }
    return 0;
}

