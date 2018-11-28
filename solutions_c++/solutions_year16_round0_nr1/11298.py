#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <limits.h>

#define MAX_N 1000000

using namespace std;

void add_to_set(int num, unordered_set<int> &digits) {
    while (num > 0 ) {
        digits.insert(num % 10);
        num /= 10;
    }
}

int solve(int N) {
    if (N == 0) return -1;
    if (N == 1) return 10;

    unordered_set<int> digits;
    int i = 0;
    while  (N * i < INT_MAX && digits.size() < 10) {
        add_to_set(N * ++i, digits);
    }

    return digits.size() == 10 ? N * i : -1;
}

int main() {
    ifstream f_in("input");
    ofstream f_out("output");

    int n_t;

    f_in >> n_t;

    int N = 0;
    int result = 0;
    for (int i = 0; i < n_t; i++) {
        f_in >> N;
        result = solve(N);
        f_out << "Case #" << i + 1 << ": " << (result == -1 ? "INSOMNIA" : to_string(result)) << endl;
    }

    f_in.close();
    f_out.close();

    return 0;
}