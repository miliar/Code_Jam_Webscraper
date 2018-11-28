#include <string>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

// replacing programming finesse with an array computed in what i have used for the small version
uint64_t fairRoots[] = {
    1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001,
    10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101,
    110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101,
    1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111,
    2000002, 2001002,
    
};

void work(uint64_t no) {
    uint64_t lower, higher;
    cin >> lower >> higher;
    uint64_t total = 0;
    for (uint64_t i = 0; i < (sizeof(fairRoots)/sizeof(fairRoots[0])); i++) {
        if (fairRoots[i]*fairRoots[i] >= lower && fairRoots[i]*fairRoots[i] <= higher)
            total++;
    }
    cout << "Case #" << no << ": " << total << endl;
}

int main(void) {
    uint64_t cases;
    cin >> cases;
    for (uint64_t i = 1; i <= cases; i++) {
        work(i);
    }
    return 0;
}