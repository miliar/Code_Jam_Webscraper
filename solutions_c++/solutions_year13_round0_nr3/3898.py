////////////////////////////////////////////////////////////////////////////////
// C.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Solves Google Code Jam Qualification Round Problem C
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  04/13/2013 17:36:24
//  Revision History:
//      04/13/2013  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>

using namespace std;

bool isPalindrome(const char *str) {
    size_t len = strlen(str);
    for (size_t i = 0; i < len; ++i) {
        if (str[i] != str[len - 1 - i]) return false;
    }

    return true;
}

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    int numTests;
    cin >> numTests;

    for (int t = 1; t <= numTests; ++t)  {
        size_t A, B, fairAndSquare;
        cin >> A >> B;

        char buffer[256];

        fairAndSquare = 0;

        size_t sqrtA = sqrt((double) A), sqrtB = sqrt((double) B);
        for (size_t sqrtCand = sqrtA; sqrtCand <= sqrtB; ++sqrtCand)  {
            size_t cand = sqrtCand * sqrtCand;
            // First, reject if we're outside the range
            if ((cand < A) || (cand > B)) continue;

            // Second, reject if sqrt is not a palindrome
            snprintf(buffer, 256, "%llu", sqrtCand);
            if (!isPalindrome(buffer)) continue;

            // Second, reject if candidate is not a palindrome
            snprintf(buffer, 256, "%llu", cand);
            if (!isPalindrome(buffer)) continue;

            ++fairAndSquare;
        }
        
        cout << "Case #" << t << ": " << fairAndSquare << endl;
    }

    return 0;
}
