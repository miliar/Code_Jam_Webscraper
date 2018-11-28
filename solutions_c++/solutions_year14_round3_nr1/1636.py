#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stack>
#include <functional>
#include <fstream>
#include <deque>
#include <queue>
#include <iostream>
#include <fstream>
#include <ctime>
#include <sstream>
#include <climits>

using namespace std;

long long gcd(long long a, long long b)
{
    while(a && b)
    {
        if(a > b)
            a %= b;
        else
            b %= a;
    }
    return a + b;
}

int main()
{
    ios_base::sync_with_stdio(0);
    fstream in("input.txt");
    fstream out("output.txt");

    int n;
    in >> n;
    for(int i = 1; i <= n; ++i)
    {
        long long a, c;
        char b;
        in >> a >> b >> c;
        while(c % 2 == 0 && a % 2 == 0)
        {
            c >>= 1;
            a >>= 1;
        }
        int gcd1 = gcd(a, c);
        c /= gcd1;
        a /= gcd1;
        int count = 0;
        long long d = c / 2;
        while(c % 2 == 0)
        {
            c >>= 1;
            ++count;
        }
        if(c != 1)
        {
            out << "Case #" << i << ": " << "impossible" << endl;
            continue;
        }
        int res = 1;
        while(d > a)
        {
            ++res;
            d >>= 1;
        }
        out << "Case #" << i << ": " << res << endl;
    }

    system("pause");
    return 0;
}