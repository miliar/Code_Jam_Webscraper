#include <iostream>
#include <gmp.h>
#include <gmpxx.h>
#include <string>
#include <fstream>
#include <cassert>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

// Build up a palindrome Z by treating integer B as a binary
// string of 0's and 1's representing left hand half.
// numBits specifies length of that string.
// centreDigit can add an additional centre digit, or -1 to omit
// and generate even-length palindrome.
mpz_class build_palindrome(unsigned long B, int numBits, int centreDigit) {
    mpz_class result;
    // do LHS first
    unsigned long mask = 1 << (numBits - 1);
    for (int i = 0; i != numBits; ++i) {
        result *= 10;
        if (B & mask) {
            result++;
        }
        mask >>= 1;
    }

    // do centre digit
    if (centreDigit != -1) {
        result *= 10;
        result += centreDigit;
    }

    // now rhs
    for (int i = 0; i != numBits; ++i) {
        result *= 10;
        if (B & 1) {
            result++;
        }
        B >>= 1;
    }
    return result;
}

bool is_palindrome(const mpz_class& p) {
    string s = p.get_str();
    string rev = s; std::reverse(rev.begin(), rev.end());
    return s == rev;
}

// Find all palindromes of length L, that when squared, are
// themselves palindromes.
// We use brute force search but we don't need to search too
// many possibilities:
//    For even length palindromes, only consider those made
//      entirely of 0's and 1's, plus 20...02
//    For odd length palindromes, it's the same, plus those
//      of 0's and 1's with a single '2' in the middle,
//      and 20...1...02 (i.e. with a single '1' in the middle)
void print_squareable(int L) {
    if (L == 1) { // special case: only 1, 2, 3.
        cout << 1 << endl;
        cout << 2 << endl;
        cout << 3 << endl;
        return;
    }

    // We'll generate palindromes of 0s and 1s by looping over
    // integers and treating them as the binary representation
    // of the first half of the palindrome.
    std::string minimumStr = "1";
    minimumStr.append(L/2 - 1, '0');
    std::string maximumStr = std::string(L/2, '1');
    mpz_class minimumZ(minimumStr, 2);
    mpz_class maximumZ(maximumStr, 2);
    assert(maximumZ.fits_uint_p());
    unsigned long minimum = minimumZ.get_ui();
    unsigned long maximum = maximumZ.get_ui();

    if (L % 2 == 0) {
        for (unsigned long i = minimum; i <= maximum; ++i) {
            mpz_class palindrome = build_palindrome(i, L / 2, -1);
            if (is_palindrome(palindrome * palindrome)) {
                cout << palindrome << endl;
            }
        }
        // This is the 20...02 case:
        unsigned long extra = 1 << ((L / 2) - 1);
        mpz_class extraP = build_palindrome(extra, L / 2, -1) * 2;
        if (is_palindrome(extraP * extraP)) {
            cout << extraP << endl;
        }
    } else {
        for (unsigned long i = minimum; i <= maximum; ++i) {
            bool hitLimit = false;
            for (int centre = 0; centre != 3; ++centre) {
                mpz_class palindrome = build_palindrome(i, L / 2, centre);
                if (is_palindrome(palindrome*palindrome)) {
                    cout << palindrome << endl;
                }
            }
        }
        // Handle 20...02 and 20..010..02:
        unsigned long extra = 1 << ((L / 2) - 1);
        mpz_class centre0 = build_palindrome(extra, L / 2, 0);
        mpz_class centre1 = build_palindrome(extra, L / 2, 1);
        mpz_class extra1 = centre0 + centre0;
        mpz_class extra2 = centre0 + centre1;
        
        if (is_palindrome(extra1 * extra1)) {
            cout << extra1 << endl;
        }
        if (is_palindrome(extra2 * extra2)) {
            cout << extra2 << endl;
        }
    }
}

// Replacement for 'main' to generate the table of all
// palindromes whose squares are palindromes, up to length 50
void main2() {
    for (int length = 1; length <= 50; ++length) {
        print_squareable(length);
    }
}

std::vector<mpz_class> FairSquares;

int num_fair_squares(const mpz_class& A, const mpz_class& B) {

    std::vector<mpz_class>::iterator itrA = std::lower_bound(FairSquares.begin(), FairSquares.end(), A);
    std::vector<mpz_class>::iterator itrB = std::upper_bound(FairSquares.begin(), FairSquares.end(), B);

    return (itrB - itrA);
}

// Using libgmp.  To build:
// g++ C.cpp -O -o solve -lgmpxx -lgmp

// Finding all solutions up to 10^100 with my code seems to
// take about 5 minutes ... just to be sure about not cutting
// time limit short, decided to dump them all out to a file
// and load that for the real thing.
// To generate table, change main to just call main2
int main()
{
    // main2();

    ifstream table("table");
    while (table) {
        mpz_class x;
        table >> x;
        if (x != 0) {
            FairSquares.push_back(x*x);
        }
    }

    istream& input = cin;
    // ifstream input("sample");

    int T;
    input >> T;
    for (int t = 0; t != T; ++t) {
        mpz_class A, B;
        input >> A >> B;

        int result = num_fair_squares(A, B);
        cout << "Case #" << t + 1 << ": " << result << endl;
    }

    return 0;
}
