#include <fstream>
#include <iostream>
#include <assert.h>
#include <string.h>
using namespace std;

int N = 16, J = 50, output = 0;
long long divisors[11];


long long isPrime(long long n) {
    if (n <= 3)
        return -1;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;
    long long i = 5;
    while (i * i <= n)
    {
        if (n % i == 0)
            return i;
        if (n % (i + 2) == 0)
            return (i + 2);
        i += 6;
    }
    return -1;
}

void controlla(char s[])
{
    //cout << s << endl;
    for (int i = 2; i <= 10; i++)
    {
        long long val = strtol(s, NULL, i);
        //cout << val << endl;
        assert(val != 0);
        divisors[i] = isPrime(val);
        assert(divisors[i] != 1);
        assert(divisors[i] != val);
        if (divisors[i] == -1)
            return;
    }
    ofstream out("output.txt", ios_base::app);
    out << s << " ";
    for (int i = 2; i <= 9; i++)
        out << divisors[i] << " ";
    out << divisors[10] << endl;
    output++;
}


void genera(int idx, char s[])
{
    if (output == J)
        return;
    if (idx == N - 1)
        controlla(s);
    else
    {
        s[idx] = '0';
        genera(idx + 1, s);
        s[idx] = '1';
        genera(idx + 1, s);
    }
}

int main()
{
    ofstream out("output.txt");
    out << "Case #1:" << endl;
    char s[17] = "1000000000000001";
    genera(1, s);
}
