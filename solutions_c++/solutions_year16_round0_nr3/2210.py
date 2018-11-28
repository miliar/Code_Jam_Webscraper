#include <iostream>
#include <stdint.h>
#include <vector>
#include <algorithm>

using namespace::std;

void add_one(vector<int>& v)
{
    for (int i = 0; i < v.size(); ++i)
    {
        if (v[i] == 0)
        {
            v[i] = 1;
            break;
        }
        else
            v[i] = 0;
    }
}

bool all_one(vector<int>& v)
{
    for (int i = 0; i < v.size(); ++i)
        if (v[i] == 0)
            return false;

    return true;
}

void print(vector<int>& v)
{
    for (int i = v.size() - 1; i >= 0; --i)
        cout << v[i];
    cout << endl;
}

int main ()
{
    vector<bool> p(10000000, true);
    p[0] = false;
    p[1] = false;
    for (int i = 0; i < 10000000; ++i)
    {
        if (!p[i]) continue;

        for (int j = 2 * i; j < 10000000; j += i)
            p[j] = false;
    }

    vector<int> prime;
    for (int i = 2; i < 10000000; ++i)
        if (p[i])
            prime.push_back(i);

    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int N, J;
        cin >> N >> J;

        cout << "Case #" << t + 1 << ":" << endl;
        int count = 0;
        vector<int> v(N, 0);
        v[0] = 1;
        v[v.size() - 1] = 1;
        bool max_reached = false;
        while (true)
        {
            vector<int> d;
            for (uint64_t b = 2; b <= 10; ++b)
            {
                for (int i = 0; i < prime.size(); ++i)
                {
                    uint64_t p = prime[i];
                    uint64_t x = v[v.size() - 1];
                    for (int i = v.size() - 2; i >= 0; --i)
                        x = ((x * b) + (uint64_t)v[i]) % p;
                    x %= p;

                    if (x == 0)
                    {
                        d.push_back(p);
                        break;
                    }
                }
            }

            if (d.size() == 9)
            {
                ++count;
                for (int j = v.size() - 1; j >= 0; --j)
                    cout << v[j];
                cout << " ";

                for (int j = 0; j < d.size(); ++j)
                    cout << d[j] << " ";
                cout << endl;
            }

            if (count == J) break;

            if (max_reached) break;
            add_one(v);
            add_one(v);
            if (all_one(v)) max_reached = true;
        }
    }
}
