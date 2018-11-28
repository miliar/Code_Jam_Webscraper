#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <limits>
#include <string>
#include <sstream>

using namespace std;

const int square_boudary = 14;
const int boudary = 7;
const int half_boundary = 4;
long long A, B, N;
set<long long> ps;

bool is_palindrome(long long a)
{
    ostringstream ss;
    ss << a;
    string s = ss.str();
    long long n = s.length() / 2;
    for (int i = 0; i < n; ++i)
    {
        if (s[i] != s[s.length() - i - 1])
        {
            return false;
        }
    }
    return true;
}

void check_string(string s)
{
    istringstream ss(s);
    long long a;
    ss >> a;
    long long sq = a * a;
    if (is_palindrome(sq))
    {
        ps.insert(sq);
    }
}

void gen(string s)
{
    string z = s;
    reverse(z.begin(), z.end());
    check_string(s + z.substr(1));
    check_string(s + z);
    if (s.length() < half_boundary)
    {
        gen(s + "0");
        gen(s + "1");
        gen(s + "2");
    }
}

void calc()
{
    ps.insert(9);
    gen("1");
    gen("2");
}

long long inside()
{
    long long sk = 0;
    for (set<long long>::iterator it = ps.begin(); it != ps.end(); ++it)
    {
        if (*it > B)
        {
            break;
        }
        if (*it >= A)
        {
            ++sk;
        }
    }
    return sk;
}

int main()
{
    ifstream fin("C-large-1.in");
    ofstream fout("C-large-1.out");
    int T;
    fin >> T;
    calc();
    for (int i = 1; i <= T; ++i)
    {
        fin >> A >> B;
        fout << "Case #" << i << ": " << inside() << endl;
    }
    return 0;
}
