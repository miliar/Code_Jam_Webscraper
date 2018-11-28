#include <iostream>
#include <stdio.h>

using namespace std;

long long prime (long long a) {


    for (int i = 3; i <= a/3; i+=2) {
        if (a%i == 0)
            return i;
        if (i == 19999999) //give up
            return 1;
        if (i == 2)
            i = 1;
    }
    return 1;
}

long long power (long long a, int b) {
    long long r = 1;
    for (int i = 1; i <= b; i++)
        r *= a;
    return r;
}
int coin [32];

int main()
{
    freopen("output.txt","w",stdout);
    int t,n,j;
    int counter = 0;
    long long sum = 0;
    bool good;
    long long divisor;
    long long divisors [9];

    cin >> t >> n >> j;

    coin[n-1] = 1;
    coin[0] = 1;

    cout << "Case #1:" << endl;
    while (1) {
        good = true;

        for (int base = 2; base <= 10; base++) {
            sum = 0;

            for (int i = 0; i < n; i++)
                sum += power(base,i)*coin[i];

            divisor = prime(sum);

            if (divisor == 1) {
                good = false;
                break;
            }
            else
                divisors[base-2] = divisor;
        }

        if (good) {
            counter++;

            for (int i = n-1; i >= 0; i--)
                cout << coin[i];
            cout << " ";
            for (int i = 0; i < 9; i++)
                cout << divisors[i] << " ";
            cout << endl;
            if (counter == j)
                break;
        }

        coin[1]++;
        for (int i = 1; i < n; i++) {
            if (coin[i] == 2) {
                coin[i] = 0;
                coin[i+1]++;
            }
        }

    }
}
