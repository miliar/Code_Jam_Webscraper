#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

int process(long long n)
{
    int flag = 0;
    while (n)
    {
        flag |= 1 << (n % 10);
        n /= 10;
    }

    return flag;
}

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n;
        cin >> n;

        int flag = 0;
        int tries = 0;

        while (flag != 1023 && tries < 300)
        {
            ++tries;
            flag |= process(1LL * tries * n);
        }

        printf("Case #%d: ", CASE);
        if (flag == 1023)
            cout << 1LL * tries * n << endl;
        else
            cout << "INSOMNIA" << endl;
    }


    return 0;
}
