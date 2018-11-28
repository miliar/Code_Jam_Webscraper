#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;
const int MAX = (1 << 17) + 5;
bool prime[MAX];
int A[MAX], dig[20], l, B[15];

void s()
{
    int i, j;
    memset(prime, false, sizeof(prime));
    memset(A, -1, sizeof(A));
    prime[0] = prime[1] = true;
    for(i = 2;i < MAX;++i)
    {
        if(prime[i] == false)
        {
            A[i] = 0;
            for(j = 2*i;j < MAX;j += i)
            {
                prime[j] = true;
                if(A[j] == -1)
                    A[j] = i;
            }
        }
    }
}

long long isPrime(long long x)
{
    if(x < MAX)
        return A[x];
    else
    {
        long long m = sqrt(x) + 1, i;
        for(i = 2;i < m;++i)
            if(x % i == 0)
            {
                return i;
            }
        return 0;
    }
}

bool isJamcoin(int base)
{
    long long x = 0, y;
    for(int i = l-1;i >= 0;--i)
        x = (x * base) + dig[i];
    y = isPrime(x);
    if(y)
    {

        B[base] = y;
        return true;
    }
    else
        return false;
}

int main()
{
    long long t, n, J, k, x, z;
    bool flag;
    s();
    cin >> t >> n >> J;
    cout << "Case #1:" << endl;
    x = (1 << (n-1)) + 1;
    for(long long i = 0, k = (1 << (n-2));i < k;++i)
    {
        z = x + (i << 1);
        l = 0;
        while(z)
        {
            dig[l++] = z & 1;
            z >>= 1;
        }
        flag = true;
        for(int j = 2;j <= 10;++j)
        {
            if(!isJamcoin(j))
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            J--;
            for(int j = l-1;j >= 0;--j)
                cout << dig[j];
            for(int j = 2;j <= 10;++j)
                cout << " " << B[j];
            cout << endl;
        }
        if(J == 0) break;
    }
    return 0;
}
