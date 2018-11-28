#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool is_palindrome(long num) {
    int digits[100];
    int num_digits = 0;

    while (num > 0) {
        digits[num_digits] = num % 10;
        num /= 10;
        num_digits++;
    }

    for (int i = 0; i < num_digits/2; i++) {
        if (digits[i] != digits[num_digits - 1 - i])
            return false;
    }

    return true;
}

vector<long> find_all_fnsqrs(long nmin, long nmax) {
    vector<long> all_fnsqrs;
    long num_fnsq = 0;

    long sqrtmin = sqrt(nmin);
    long sqrtmax = sqrt(nmax);
    long square;
    //cout << "nmin: " << nmin << ", nmax: " << nmax << endl;
    //cout << "sqrtmin: " << sqrtmin << ", sqrtmax: " << sqrtmax << endl;

    for (long i = sqrtmin; i <= sqrtmax; i++) {
        if (is_palindrome(i)) {
            square = i * i;
            if (square < nmin || square > nmax)
                continue;
            if (is_palindrome(square)) {
                num_fnsq++;
                all_fnsqrs.push_back(square);
            }
        }
    }

    //cout << num_fnsq;

    return all_fnsqrs;
}

void process_interval(long nmin, long nmax, vector<long> &all_fnsqrs) {
    long num_fnsq = 0;

    for (long &l : all_fnsqrs) {
        if (nmin <= l && nmax >= l)
            num_fnsq++;
    }

    cout << num_fnsq;
}

int main(int argc, char **argv) {
    int num_testcases;
    ifstream f(argv[1]);

    f >> num_testcases;

    vector<long> all_fnsqrs = find_all_fnsqrs(1, 100000000000000);

    //for (long &l : all_fnsqrs)
        //std::cout << l << endl;

    for (int i = 0; i < num_testcases; i++) {
        cout << "Case #" << (i+1) << ": ";
        long nmin, nmax;
        f >> nmin;
        f >> nmax;
        process_interval(nmin, nmax, all_fnsqrs);
        cout << endl;
    }
}
