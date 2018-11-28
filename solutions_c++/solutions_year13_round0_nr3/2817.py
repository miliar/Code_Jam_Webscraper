/*
Problem

Little John likes palindromes, and thinks them to be fair (which is a fancy word
for nice). A palindrome is just an integer that reads the same backwards and
forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are
not (even though 010=10, we don't consider leading zeroes when determining
whether a number is a palindrome).

He recently became interested in squares as well, and formed the definition of a
fair and square number - it is a number that is a palindrome and the square of
a palindrome at the same time. For instance, 1, 9 and 121 are fair and square
(being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and
676 are not fair and square: 16 is not a palindrome, 22 is not a square, and
while 676 is a palindrome and a square number, it is the square of 26, which
is not a palindrome.

Now he wants to search for bigger fair and square numbers. Your task is, given an
interval Little John is searching through, to tell him how many fair and square
numbers are there in the interval, so he knows when he has found them all.

Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This
problem has 1 Small input and 2 Large inputs. Once you have solved the Small
input, you will be able to download any of the two Large inputs. As usual, you
will be able to retry the Small input (with a time penalty), while you will get
only one chance at each of the Large inputs.


Input

The first line of the input gives the number of test cases, T.
T lines follow. Each line contains two integers, A and B - the endpoints of the
interval Little John is looking at.

Output

For each test case, output one line containing "Case #x: y", where x is the case
number (starting from 1) and y is the number of fair and square numbers greater
or equal to A and smaller or equal than B.

Limits

Small dataset

1 <= T <= 100.
1 <= A <= B <= 1000.

First large dataset

1 <= T <= 10000.
1 <= A <= B <= 10^14.

Second large dataset

1 <= T <= 1000.
1 <= A <= B <= 10^100.

Sample

Input 
 
3
1 4
10 120
100 1000
 
Output 

Case #1: 2
Case #2: 0
Case #3: 2

[Solution]

1. Squares end with the digit {1 4 5 6 9}


*/

#include <iostream>
#include <set>
#include <cmath>

using namespace std;

long long int CountFairSquares(long long int A, long long int B);
bool IsPalindrome(long long int n);
long long int IsPerfectSquare(long long int n);

int main(void)
{
    int T;
    cin >> T;
    int testcase_id = 1;
    while (T--) {
        long long int A, B;
        cin >> A >> B;
        cout << "Case #" << testcase_id++ << ": " << CountFairSquares(A, B) << endl;
    }
    return 0;
}

bool IsPalindrome(long long int n)
{
    int* digits = new int[101];
    int i = -1;
    do {
        digits[++i] = n % 10;
        n = n / 10;
    } while (n != 0);

    int j = 0;
    bool is_a_palindrome = true;
    while (j < i) {
        if (digits[i] != digits[j]) {
            is_a_palindrome = false;
            break;
        }
        ++j;
        --i;
    }
    delete [] digits;
    return is_a_palindrome;
}

long long int IsPerfectSquare(long long int n)
{
    set<long long int> seen;
    long long int x = n / 2;
    if (!x) return 1;
    seen.insert(x);
    while (x * x != n) {
        x = (x + n / x) / 2;
        if (seen.count(x))
            return -1;
        seen.insert(x);
    }
    return x;
}

long long int CountFairSquares(long long int A, long long int B)
{
    long long int a = IsPerfectSquare(A);
    if (-1 == a)
        a = static_cast<long long int>(ceil(sqrt(A)));
    long long int b = IsPerfectSquare(B);
    if (-1 == b)
        b = static_cast<long long int>(floor(sqrt(B)));
    long long int count = 0;
    for (long long int i = a; i <= b; ++i)
        if (IsPalindrome(i) && IsPalindrome(i*i))
            ++count;
    return count;
}

