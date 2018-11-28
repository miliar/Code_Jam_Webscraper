#include <iostream>
#include <vector>

using namespace std;

long long calc(long long n) {
    vector<bool> digits(10, false);
    for (long long i = 1; ; i++) {
        long long num = i * n;
        long long currentNumber = num;
        while (num > 0) {
            digits[num % 10] = true;
            num /= 10;
        }
        bool allTrue = true;
        for (bool b : digits) {
            allTrue = allTrue && b;
        }
        if (allTrue) {
             return currentNumber; 
        }
    }
}

int main() {
	int testCases;
	long long N; 
    cin >> testCases;

    for (int i = 1; i <= testCases; i++) {
        cin >> N;
        cout << "Case #" << i << ": ";
        if (N == 0) {
            cout << "INSOMNIA";
        }else {
            cout << calc(N);
        }
        cout << endl;
    }

    return 0;
}
