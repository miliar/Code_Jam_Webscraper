#include <bits/stdc++.h>
using namespace std;

/// Prototypes
bool binGen(long long int k, long long int n);
bool solve();
bool prime(long long int numToTest);
long long int power(long long int a, long long int b);

/// Global Declarations
long long int n, j, currNumbers = 0, num[25] = {1};
long long int arr[25];

ofstream outfile;
ifstream inpfile;

int main()
{
    inpfile.open("C-small-attempt1.in");
    outfile.open("prob1.txt");

    int t;
    inpfile >> t;

    inpfile >> n >> j;
    outfile << "Case #1:" << endl;

    num[0] = 1;
    num[n - 1] = 1;
    binGen(1, n - 2);

    outfile.close();
    inpfile.close();
    return 0;
}

bool binGen(long long int k, long long int m)
{
    /// Base Case
    if (k == m)
    {
        if(solve() == true)
            return true;
        return false;
    }

    num[k] = 0;
    if(binGen(k + 1, m))
        return true;
    num[k] = 1;
    if(binGen(k + 1, m))
        return true;
}

bool solve()
{
    long long int numToTest = 0;
    for (long long int base = 2; base <= 10; base++)
    {
        long long int counter = 0;
        numToTest = 0;
        for (long long int i = n - 1; i >= 0; i--)
        {
            numToTest += (num[i]) * power(base, counter);
            counter++;
        }

        if (prime(numToTest) == true)
        {
            return false;
        }
        else
        {
            for (long long int i = 2; i < numToTest; i++)
            {
                if (numToTest % i == 0)
                {
                    arr[base] = i;
                    break;
                }
            }
        }
    }

    currNumbers++;
    for (long long int i = 0; i < n; i++)
        outfile << num[i];
    outfile << " ";
    for (long long int i = 2; i <= 10; i++)
        outfile << arr[i] << " ";
    outfile << endl;

    if (currNumbers == j)
        return true;
    else
        return false;
}

bool prime(long long int numToTest)
{
    long long int upper = sqrtl(numToTest) + 1, f = 0;
    for (long long int i = 2; i <= upper; i++)
    {
        if (numToTest % i == 0)
        {
            f = 1;
            break;
        }
    }

    if (f == 1)
        return false;
    else
        return true;
}

long long int power(long long int a, long long int b)
{
    if (b == 0)
        return 1;

    long long int aa = a;
    for (int i = 1; i < b; i++)
        aa *= a;
    return aa;
}
