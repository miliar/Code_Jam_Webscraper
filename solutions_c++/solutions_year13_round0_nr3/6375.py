#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
#include <sstream>

using namespace std;

int count_fair_squared(long long a, long long b);
bool is_palindrome(long long n);

// Tests if a given number is a palindrome.
bool is_palindrome(long long n)
{
    // Convert n to string
    string n_str;
    stringstream ss;
    ss << n;
    n_str = ss.str();

    // Test if palindrome
    unsigned int i;
    
    for (i = 0; i < n_str.length() / 2; i++)
    {
        if (n_str[i] != n_str[n_str.length() - i - 1])
            return false;
    }
    return true;
}

// Counts the number of fair square integers between a and b.
int count_fair_squares(long long a, long long b)
{
    int count = 0;

    // Start at the square root of a, end at the square root of b.
    long long n = sqrt(a);
    long long end = sqrt(b) + 1;

    // Clean up the edge case...
    if (n * n != a)
        n++;

    while (n < end)
    {
        if (is_palindrome(n) && is_palindrome(n * n))
            count++;
        n++;
    }

    return count;
}


int main(int argc, char *argv[])
{
    ifstream infile;
    ofstream outfile;

    infile.open(argv[1], fstream::in);
    outfile.open("fs.out", fstream::out);

    // Number of test cases
    int t;
    infile >> t;

    // A is the lower bound, B is the upper bound.
    long long a, b;

    int i;
    for (i = 0; i < t; i++)
    {
        infile >> a;
        infile >> b;

        outfile << "Case #" << i + 1 << ": " << count_fair_squares(a, b);
        
        if (i != t - 1)
            outfile << '\n';
    }


    infile.close();
    outfile.close();
    return 0;
}
