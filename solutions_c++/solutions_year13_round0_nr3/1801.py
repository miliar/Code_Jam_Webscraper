#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;
unsigned long long A, B;

unsigned long long fairPalin[] = { 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 
1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 
404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 
1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 
100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, };

int fairPalinLength = sizeof(fairPalin)/sizeof(unsigned long long);

bool isPalin(unsigned long long n)
{
    char num[100];
    sprintf(num, "%llu", n);
    int l = strlen(num);
    for  (int i = 0; i < l/2; i++)
    {
        if (num[i] != num[l-i-1])
        {
            return false;
        }
    }

    return true;
}

void solve(int test)
{
    // read test input
    cin >> A >> B;

    // Count
    int numFairPalin = 0;
    for (int i = 0; i < fairPalinLength; i++)
    {
        if (A <= fairPalin[i]  && fairPalin[i] <= B)
            numFairPalin++;
    }
    cout << "Case #" << test << ": " << numFairPalin << endl; 
}

void generateFairPair(int test)
{
    // read test input
    cin >> A >> B;

    int t  = 0;

    cout << "unsigned long long fairPalin[] = { ";
    for (unsigned long long i = 1; i <= pow(10, 16); i++)
    {
        if (isPalin(i))
        {
            unsigned long long p = pow(i, 2);
            if (isPalin(p))
            {
                cout << p << ", ";
                t++;
                if (t % 10 == 0)
                {
                    cout << endl;
                }
            }
            if (p > pow(10, 16)) 
            break;
        }        
    }
    cout << "};" << endl;
    cout << t << endl;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cout << "Usage: %s inputfile" << argv[0];
        return 1;
    }
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests = 0;
    cin >>  tests;

    //generateFairPair(1);
    for (int i = 1; i <= tests; i++)
        solve(i);

    return 0;
}