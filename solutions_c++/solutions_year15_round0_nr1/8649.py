#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <gmpxx.h>


using namespace std;

void alg() {
    int n, sInt, currentUp = 0, result = 0;
    char sChar;
    cin >> n;
    
    for (int i = 0; i <= n; i++) {
        cin >> sChar;
        sInt = sChar - '0';
        if (currentUp < i) {
            result += i - currentUp;
            sInt += i - currentUp;
        }
        currentUp += sInt;
    }
    
    cout << result << endl;
}

int main() {
    int n_cases;
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
        cout << "Case #" << test_case << ": ";
        alg();
    }
    
    return EXIT_SUCCESS;
}
