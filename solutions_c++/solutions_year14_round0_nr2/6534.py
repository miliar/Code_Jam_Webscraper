// clang++ -std=c++11 -stdlib=libc++ -Wall -o cookie cookie.cpp
// ./cookie < input-small.txt 2>log.txt 1>output.txt

// test with digamma boost

#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
    int size;
    double C, F, X;

    cout << fixed;
    cerr << fixed;
    
    cin >> size;
    for (int index = 1; index <= size; ++index) {
        cerr << "\nCase #" << index << '\n'; 
        cin >> C;
        cin >> F;
        cin >> X;

        double sum = 0.0;
        double money = 2.0;
        double time = X / money;
        for (;;) {
            double dT = C / money;
            sum += dT; 

            money += F;
            double remainder = X / money;

            if (time < (sum + remainder)) {
                cout << "Case #" << index << ": ";
                cout.precision(7);
                cout << time << '\n';
                cerr << "Case #" << index << ": ";
                cerr.precision(7);
                cerr << time << '\n';
                break;
            }
            else {
                time = sum + remainder;
                cerr << "Time: ";
                cerr.precision(7);
                cerr << time << '\n';
            }
        }
    }
}
