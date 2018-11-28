//Eldar Gaynetdinov

#include <bits/stdc++.h>
using namespace std;

constexpr int B = 14;
constexpr int U = 1 << B;

uint64_t get_num(int k, uint64_t b)
{
    uint64_t q = b;

    uint64_t num = 1;

    for(uint64_t i = 0; i < B; i++)
    {
        if(k & (1 << i)) num += q;

        q *= b;
    }

    num += q;

    return num;
}

int first_div(uint64_t num)
{
    for(int i = 2; i < 1000; i++)
        if(num % i == 0) return i;

    return 0;
}

vector<int> f(int k)
{
    vector<int> v;

    for(int b = 2; b <= 10; b++)
    {
        int d = first_div( get_num(k, b) );

        if(d) v.push_back(d);
    }

    return v;
}

int main()
{
    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        int N, J; cin >> N >> J;

        cout << "Case #" << t << ":" << endl;

        for(int i = 0; i < U && J; i++)
        {
            vector<int> v = f(i);

            if(v.size() != 9) continue;

            J--;

            bitset<B> b(i);

            cout << 1 << b << 1 << ' ';

            for(int j = 0; j < 9; j++)
            {
                cout << v[j];

                if(j < 8) cout << ' ';
            }

            cout << endl;
        }
    }

    return 0;
}
