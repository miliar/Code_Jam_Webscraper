#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <iterator>
#include <bitset>
using namespace std;

string to_bin(unsigned long long int x)
{
    return bitset< 16 >(x).to_string();
}

unsigned long long int to_int(const string& s, int base)
{
    unsigned long long int result = 0;
    unsigned long long int factor = 1;
    for (int i = s.size()-1; i >= 0; --i)
    {
        int bit = s[i] - '0';
        unsigned long long int value = factor * bit;
        result += value;
        factor *= base;
    }
    return result;
}

unsigned long long int find_divisor(unsigned long long int n)
{
    int max_tries = 100;
    int tries = 0;


    for (int candidate = 2; tries++ < max_tries; candidate++)
        if (n%candidate == 0)
            return candidate;
    return -1;
}

vector<unsigned long long int> divisors(unsigned long long int x, string& s)
{
    vector<unsigned long long int> result;
    for(int base = 2; base <= 10; ++base)
    {
        unsigned long long int n = to_int(s, base);
        unsigned long long int d = find_divisor(n);
        if (d == -1)
            return result;
        result.push_back(d);
    }
    return result;
}

map<string, vector<unsigned long long int>> generate(int n, int j)
{
    map<string, vector<unsigned long long int>> result;

    string s = "1000000000000001";
    unsigned long long int x = to_int(s,10);

    while(result.size() < j)
    {
        vector<unsigned long long int> d = divisors(x, s);
        if (d.size() == 9)
        {
            //cerr << "!";
            result[s] = d;
        }
        else
        {
            //cerr << ".";
        }
        x += 2;
        s = to_bin(x);
    }
    return result;
}

int main()
{
    int test_cases;
    cin >> test_cases;
    for (int t = 0; t < test_cases; ++t)
    {
        int n;
        int j;
        cin >> n >> j;

        auto result = generate(n, j);
        cout << "Case #" << t + 1 << ":" << endl;
        for (auto r : result)
        {
            cout << r.first << " ";
            copy(r.second.begin(), r.second.end(), ostream_iterator<int>(cout, " "));
            cout << endl;
        }
    }

}
