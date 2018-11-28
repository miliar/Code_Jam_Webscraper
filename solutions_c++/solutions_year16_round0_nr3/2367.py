#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;
typedef unsigned long long uint64;

uint64 n;

uint64 modular_exp(uint64 a, uint64 b, uint64 n){
    uint64 t = a % n;
    uint64 ret = 1LL;
    while (b) {
        if (b & 1LL)
            ret = (ret * t) % n;
        t = (t * t) % n;
        b >>= 1;
    }
    return ret;
}

bool MillerRabbin(uint64 n){
    for(int i = 0; i < 10; i++){
        uint64 a = rand() % (n - 2LL) + 2LL;
        if (modular_exp(a, n - 1LL, n) != 1LL) return 0;
    }
    return 1;
}

uint64 exps[11][33];

int main()
{
    srand(88882);
    int N = 16, J = 50;
    cout << "Case #1: " << endl;
    for (int i = 1; i <= 10; i++)
    {
        exps[i][0] = 1;
        for (int j = 1; j < 33; j++)
            exps[i][j] = exps[i][j - 1] * i;
    }
    for (int i = 0; i < J;)
    {
        uint64 n = (1 << (N - 1)) + 1 + 2 * (rand() % (1 << (N - 2)));
        bool can = true;
        for (int j = 2; j <= 10; j++)
        {
            uint64 res = 0;
            for (int k = 0; k < N; k++)
                res += ((n >> k) % 2) * exps[j][k];
            if (MillerRabbin(res))
            {
                can = false;
                break;
            }
        }
        ostringstream ost;
        if (can)
        {
            for (int k = 1; k <= N; k++)
                ost << (n >> (N - k)) % 2;
            ost << " ";
            bool err = false;
            for (int j = 2; j <= 10; j++)
            {
                uint64 res = 0;
                for (int k = 0; k < N; k++)
                    res += ((n >> k) % 2) * exps[j][k];
                bool x = false;
                for (uint64 k = 2; k * k <= res; k++)
                    if (res % k == 0)
                    {
                        ost << k;
                        x = true;
                        break;
                    }
                if (!x)
                    err = true;
                if (j != 10)
                    ost << " ";
            }
            if (!err)
            {
                cout << ost.str() << endl;
                i++;
            }
        }
    }
}