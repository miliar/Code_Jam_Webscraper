// RCC_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <algorithm>
#include <time.h>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int x, r, c;
        cin >> x >> r >> c;
        if (r * c % x != 0)
        {
            cout << "Case #" << t + 1 << ":  RICHARD" << endl;
            continue;
        }
        if (x > 6)
        {
            cout << "Case #" << t + 1 << ":  RICHARD" << endl;
            continue;
        }
        if (min(r, c) < x - 1)
            cout << "Case #" << t + 1 << ":  RICHARD" << endl;
        else
            cout << "Case #" << t + 1 << ":  GABRIEL" << endl;
    }
	return 0;
}

