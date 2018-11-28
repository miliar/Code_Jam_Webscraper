// Google Code Jam 2013
// Written by Aaron Zhou on 2013-04-13
// Problem C. Fair and Square
// https://code.google.com/codejam/contest/2270488/dashboard#s=p2

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
using namespace std;

bool isPalindrome(long long n)
{
    long long palindrome = 0;
    int m = n;
    while(n != 0)
    {
        palindrome = palindrome * 10 + n % 10;
        n /= 10;
    }
    return m == palindrome;
}

bool isFairSquare(long long n)
{
    long long i = (long long)sqrt(n);
    return ((i * i == n) && isPalindrome(i) && isPalindrome(n));
}

bool fairSquareFlag[1001];
void init()
{
    fairSquareFlag[1] = true;
    for(int i = 2; i <= 1000; ++i)
    {
        fairSquareFlag[i] = isFairSquare(i);
    }
}

int main()
{
    init();
    ifstream infile("C-small-attempt0.in", ios::in);
    ofstream outfile("pc.out", ios::out);
    int t;
    infile >> t;
    for(int k = 1; k <= t; ++k)
    {
        int from, to;
        infile >> from >> to;
        int count = 0;
        for(int i = from; i <= to; ++i)
        {
            if(fairSquareFlag[i])
            {
                ++count;
            }
        }
        outfile << "Case #" << k << ": " << count << endl;
    }
    return 0;
}
