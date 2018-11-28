#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char* argv[])
{

    int testsNumber;
    cin >> testsNumber;

    for (int testIndex = 0; testIndex < testsNumber; ++testIndex)
    {
        cout << "Case #" << testIndex + 1 << ": ";

        int k;
        cin >> k;
        string s;
        cin >> s;

        int add = 0;
        int current = 0;

        for (int i = 0; i <= k; ++i)
        {
            int t = s[i] - '0';
            if (!t)
                continue;
            if (current < i)
            {
                add += i - current;
                current = i;
            }
            current += t;
        }


        cout << add;
        cout << endl;
    }


    return 0;
}