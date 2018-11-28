// =========================================================
//
//       Filename:  Fair and Square
//
//    Description:
//
//        Version:  1.0
//        Created:  04/13/2013
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/13/2013
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

bool is_palindromes(unsigned long long int p)
{
    unsigned long long int foo = p;
    unsigned long long int tmp = 0;

    while(foo != 0) {
        tmp *= 10;
        tmp += foo%10;
        foo /= 10;
    }
    if(tmp == p)
        return true;
    return false;
}

// odd digits
void compute_palindromes_1(vector< unsigned long long int > &palindromes)
{
    // single digit
    for (unsigned int i = 1; i <= 3; ++i)
        palindromes.push_back(i*i);

    // multiple digits
    for (unsigned int i = 10; i <= 10000; ++i)
    {
        unsigned long long int half = i/10;
        unsigned long long int p = i;
        while (half > 0)
        {
            p *= 10;
            p += half%10;
            half /= 10;
        }
        if (is_palindromes(p*p))
        {
            palindromes.push_back(p*p);
        }
    }
}

// even digits
void compute_palindromes_2(vector< unsigned long long int > &palindromes)
{
    for (unsigned int i = 1; i <= 10000; ++i)
    {
        unsigned long long int half = i;
        unsigned long long int p = i;
        while (half > 0)
        {
            p *= 10;
            p += half%10;
            half /= 10;
        }
        if (is_palindromes(p*p))
            palindromes.push_back(p*p);
    }
}


unsigned long long int solve(unsigned int N, unsigned int K, vector< unsigned long long int >::iterator a)
{
    unsigned long long int result = 0l;

    return result;
}

int main()
{
    vector< unsigned long long int > palindromes;

    // pre-computation
    palindromes.clear();
    compute_palindromes_1(palindromes);
    compute_palindromes_2(palindromes);
    sort(palindromes.begin(), palindromes.end());

    // load input
    unsigned int case_no;
    cin >> case_no;

    for (unsigned int t = 0; t < case_no; ++t)
    {
        unsigned long long int A;
        unsigned long long int B;

        cin >> A >> B;

        // sove problem
        std::vector<unsigned long long int>::iterator low,up;
        low = lower_bound(palindromes.begin(), palindromes.end(), A);
        up = lower_bound(palindromes.begin(), palindromes.end(), B+1);

        cout << "Case #" << t+1 << ": ";
        cout << up-low << endl;
    }

    return 0;

}
