// Compile with: clang++ -std=c++11 -stdlib=libc++ example.cpp

/*
 * SORTING
 *
 * Ex. 1
 * sort(intVec.begin(), intVec.end());
 *
 * Ex. 2
 * bool wayToSort(int i, int j) { return i > j; }
 * sort(intVec.begin(), intVec.end(), wayToSort);
 *
 * Ex. 3
 * sort(intArray, intArray + SIZE);
 */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <vector>
#include <string>

using namespace std;

#define ULLI unsigned long long int

int calculate_flips(string& stack) {
    int num_flips = 0;
    // Initial
    int flat_ctr = 0;
    for (int i = 0; i < stack.size(); ++i) {
        if (stack[i] == '+') break;
        ++flat_ctr;
    }
    if (flat_ctr) ++num_flips;

    // Rest of stack
    for (int i = flat_ctr; i < stack.size(); ++i) {
        if (stack[i] == '-') {
            int j = i + 1;
            while (j < stack.size() && stack[j] == '-') {
                ++j;
            }
            num_flips += 2;
            i = j;
        }
    }

    return num_flips;
}

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string pancake_stack;
        cin >> pancake_stack;

        cout << "Case #" << t <<": "<<  calculate_flips(pancake_stack) << endl;
    }
    return 0;
}
