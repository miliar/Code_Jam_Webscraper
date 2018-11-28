#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <cstdio>
#include <cassert>
#include <unordered_set>
#include <cstdlib>

using namespace std;

#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define all(n) n.begin(), n.end()

// I solve this problem with two properties of integers.
// Firstly, if b % n == 1, then any number whose digits sum a
// multiple of n is multiple of n in base b. Since the input numbers only have
// zeroes and ones, I make sure that the numbers have exactly 6 ones so they
// are multiple with 2 or 3 in bases 3, 4, 5, 7, 9, and 10 (in the small case),
// or that they have exactly 15 ones so they are multiple of 3, 6, 7, and 9 (in
// the large one).
// Secondly, if b % n == a, then any number in base b modulo n will be the same
// than that number in base a modulo n. This way I only have to iterate in a
// few bases: 2 and 6 in the small case and 2 and 3 in the large one.

// This code probably needs some big refactoring.

long base(const vector <bool> &v, int b)
{
    long r = 1;
    fore(i, v)
    {
        r *= b;
        r += v[i];
    }

    return r * b + 1;
}

bool test_t(int t, const vector <bool> &g)
{
    switch (t)
    {
        case 15:
            return base(g, 2) % 3 == 0 && base(g, 2) % 7 == 0 && base(g, 3) % 7 == 0;

        case 6:
            return base(g, 2) % 3 == 0 && base(g, 6) % 7 == 0;

        default:
            throw domain_error("Invalid t!");
    }
}

vector <vector <bool>> generate_t(int t, int n, int c)
{
    vector <vector <bool>> r;

    vector <bool> g(n - t, 0);
    forn(i, t - 2)
        g.push_back(1);

    do
    {
        if (test_t(t, g))
        {
            r.push_back(g);
            if (r.size() == c)
                return r;
        }
    }
    while (next_permutation(all(g)));

    cerr << "Incomplete!" << endl;
    return r;
}

string multiples_t(int t)
{
    switch (t)
    {
        case 15:
            return "3 7 3 3 5 3 3 7 3";

        case 6:
            return "3 2 3 2 7 2 3 2 3";

        default:
            throw domain_error("Invalid t!");
    }
}

int getT(int n)
{
    switch (n)
    {
        case 32:
            return 15;

        case 16:
            return 6;

        default:
            throw domain_error("Invalid n!");
    }
}

string toString(const vector <bool>& k)
{
    string r(k.size(), '.');
    fore(i, k)
        r[i] = k[i] + '0';

    return "1" + r + "1";
}

int main()
{
    int t; cin >> t;

    forsn(z, 1, t + 1)
    {
        int n, j;
        cin >> n >> j;

        int t = getT(n);

        vector <vector <bool>> numbers = generate_t(t, n, j);
        printf("Case #%d:\n", z);
        for (const auto& k : numbers)
            printf("%s %s\n", toString(k).c_str(), multiples_t(t).c_str());
    }

    return 0;
}
