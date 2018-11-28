#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main(int argc, char* argv[])
{
    int testCount;
    cin >> testCount;

    forn(test, testCount)
    {
        long long n;
        cin >> n;

        set<long long> used;
        set<int> digits;
        long long result = -1;

        for (int i = 1;; i++)
        {
            long long m = n * i;
            if (used.count(m))
                break;
            used.insert(m);
            if (m == 0)
                digits.insert(m);
            else    
                while (m > 0)
                    digits.insert(m % 10), m /= 10;

            if (digits.size() == 10)
            {
                result = i * n;    
                break;
            }
        }

        if (result == -1)
            cout << "Case #" << (test + 1) << ": INSOMNIA" << endl;
        else
            cout << "Case #" << (test + 1) << ": " << result << endl;
    }

    return 0;
}
