/*

https://code.google.com/codejam/contest/6254486/dashboard

Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

*/

#include <iostream>
#include <vector>

using namespace std;

void addDigits(vector<int> *nums, uint64_t num) {
    uint64_t left = num;
    while (left > 0) {
        size_t digit = left % 10;
        (*nums)[digit] = 1;
        left /= 10;
    }
}

bool isDone(const vector<int> &nums) {
    for (auto n : nums) {
        if (0 == n) return false;
    }
    return true;
}

int main ()
{
    int tests;

    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        uint64_t N, currNum = 0;
        cin >> N;

        vector<int> seenNums(10);
        bool        done = false;
        int     numTries = 0;

        if (0 != N) {
            while (!done && ++numTries < 999999) {
                currNum += N;
                addDigits(&seenNums, currNum);
                done = isDone(seenNums);
            }
        }

        cout << "Case #" << test << ": ";
        if (done) { cout << currNum; }
        else { cout << "INSOMNIA"; }
        cout << endl;
    }
}
