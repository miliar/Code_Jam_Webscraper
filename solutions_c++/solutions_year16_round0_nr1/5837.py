#include <iostream>
using namespace std;

void solve()
{
    uint64_t n;
    cin >> n;

    if (n == 0)
    {
        cout << "INSOMNIA";
        return;
    }


    unsigned int digits = 0;
    for (size_t i = 0; i < 10; ++i) digits |= 1<<i;

    uint64_t cn;
    for(cn = n; ; cn += n)
    {
        for(uint64_t t = cn; t != 0; t /= 10)
        {
            unsigned d = t % 10;
            digits &= ~(1<<d);
        }

        if (!digits) break;
    }

    if (cn < n)
    {
        std::cout << "Overflow!" << std::endl;
        exit(0);
    }
    
    std::cout << cn;
}

int main()
{
    size_t T;
    cin >> T; 

    for (size_t i = 1; i < T+1; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}

