#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <string>
#include <bitset>
#include <sstream>
#include <iterator>

using namespace std;

vector<int> genPrimes()
{
    vector<int> ans;
    vector<bool> primes(1ll << 30, true);
    primes[0] = primes[1] = false;
    for (size_t i = 0; i < primes.size(); ++i)
        if (primes[i])
        {
            ans.emplace_back(i);
            for (size_t j = i * i; j < primes.size(); j += i)
                primes[j] = false;
        }
    return ans;
}

int main() 
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int TESTS;
    in >> TESTS;
    auto primes = genPrimes();
    copy(primes.begin(), primes.end(), ostream_iterator<decltype (primes)::value_type>(out, " "));
    return 0;
    for (auto TEST = 1; TEST <= TESTS; ++TEST)
    {
        out << "Case #" << TEST << ": ";
        int cur = 0;
        //in >> n >> j;
        const int n = 30, j = 500;
        for (size_t i = 0; i < (1ll << n) && cur < j; ++i)
        {
            int num;
            stringstream SS;
            SS << '1' << bitset<n>(i) << '1';
            vector<int> ans;
            for (int j = 2; j <= 10; ++j)
            {
                for (auto x : SS.str())
                    num = num * j + x - '0';
                bool ok = false;
                size_t k = 0;
                for (; k < primes.size() && !ok && primes[k] * primes[k] <= num; ++k)
                    ok |= (num % primes[k] == 0);
                if (ok)
                    ans.emplace_back(primes[k - 1]);
            }
            if (ans.size() == 10 - 2 + 1)
            {
                out << endl;
                out << SS.str() << ' ';
                copy(ans.begin(), ans.end(), ostream_iterator<decltype (ans)::value_type>(out, " "));
                ++cur;
                cerr << '\r' << cur;
                cerr.flush();
            }
        }
        out << endl;
    }
}

/*
>>> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> def check(n):
...     global primes
...     for x in primes:
...         if x * x > n:
...             return None
...         if n % x == 0:
...             return x
...
>>> def f():
...     total = 0
...     with open(r'C:\Users\vient\Desktop\ans1.txt', 'w') as f:
...         for i in range(1000000000000):
...             ans = []
...             s = '1' + bin(i)[2:].rjust(30, '0') + '1'
...             for j in range(2, 11):
...                 n = 0
...                 for c in s:
...                     n = n * j + int(c)
...                 x = check(n)
...                 if x:
...                     ans.append(x)
...             if len(ans) == 10 - 2 + 1:
...                 kek = f.write('1' + bin(i)[2:].rjust(30, '0') + '1 ' + ' '.join(map(str, ans)) + '\n')
...                 total += 1
...                 print('\r' + str(total), end='')
...             if total == 500:
...                 break
...
>>> f()
*/