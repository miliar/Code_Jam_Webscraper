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

int n, t;
vector<int> c;

bool ok(long long m)
{
    c.clear();
    //cout << m << endl;

    for (int d = 2; d <= 10; d++)
    {
        long long mul = 1;
        long long sum = 0;
        forn(i, n)
        {
            if (m & (1LL << i))
                sum += mul;
            mul *= d;
        }

        bool prime = true;
        for (long long div = 2; div * div <= sum; div++)
            if (sum % div == 0 && sum > div)
            {
                c.push_back(div);
                prime = false;
                break;
            }

        if (prime)
            return false;
    }
    
    return true;
}

int main(int argc, char* argv[])
{
    int testCount;
    cin >> testCount;

    forn(test, testCount)
    {
        cin >> n >> t;
        set<vector<long long>> s;

        while (s.size() < t)
        {
            long long i = (1) | (1 << (n - 1));
            for (int j = 1; j + 2 < n; j++)
                if (rand() % 2)
                    i |= (1LL << j);
            if (ok(i))
            {
                vector<long long> now(1, i);
                for (auto x: c)
                    now.push_back(x);                
                s.insert(now);
            }
        }

        cout << "Case #" << (test + 1) << ":" << endl;

        for (auto x: s)
        {
            bool first = true;
            for (auto xx: x)
            {
                if (first)
                {
                    string s;
                    int y = xx;
                    while (y)
                    {
                        s += char('0' + (y & 1));
                        y /= 2;
                    }
                    reverse(s.begin(), s.end());
                    cout << s;
                    first = false;
                }
                else
                    cout << " " << xx;
            }                    
            cout << endl;
        }
        //cout << endl;
    }

    return 0;
}
