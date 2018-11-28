#include <iostream>
#include <string>
#include <cmath>

using namespace std;

long long notPrime(long long x)
{

    long long sqr = floor(sqrt(x));
    for (long long i = 2; i <= sqr; ++i) {
        if (x%i == 0) {
            return i;
        }
    }

    return -1;
}

long long getCS(long long x, long long cs)
{
    long long res = 0;
    long long mul = 1;

    for (;x != 0; mul *= cs, x >>= 1) {
        if (x&1) {
            res += mul;
        }
    }

    return res;
}

void solved(long long n, long long j)
{
    long long store [10];
    long long r = (1ll<<(n-1ll));

    for (long long i = 0; i < j; ) {
        if (r&1) {
            bool flag = true;
            for (long long cs = 2; cs <= 10; ++cs) {
                long long tmp = getCS(r, cs);
                long long checkPrime = notPrime(tmp);

                if (checkPrime != -1ll) {
                    store[cs-2] = checkPrime;
                } else {
                    flag = false;
                }
            }

            if (flag == true) {
                ++i;
                cout<<getCS(r, 10);
                for (int kq = 0; kq < 9; ++kq) {
                    cout<<" "<<store[kq];
                }

                cout<<endl;
            }
        }

        ++r;
    }
}

int main()
{
    int t;
    long long n, j;
    cin>>t;

    for (int i = 1; i <= t; ++i) {
        cin>>n;
        cin>>j;
        cout<<"Case #"<<i<<":"<<endl;
        solved(n, j);
    }
    return 0;
}
