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
        string s;
        cin >> s;
        s += "+";
        int result = 0;
        for (int i = 0; i + 1 < s.length(); i++)
            if (s[i] != s[i + 1])
                result++;
        cout << "Case #" << (test + 1) << ": " << result << endl;
    }

    return 0;
}
