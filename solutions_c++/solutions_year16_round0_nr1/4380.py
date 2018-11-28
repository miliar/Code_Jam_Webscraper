#include <iostream>
#include <unordered_set>
#define MAX_FACTOR 1000

using namespace std;

void update_digits(long long number, unordered_set<int> &digits) {
    while(number != 0) {
        digits.insert(number%10);
        number /= 10;
    }
}

long long compute(long long number) {
    if(number == 0)
        return -1;
    unordered_set<int> digits;
    for(long long i = 1 ; i < MAX_FACTOR ; i++) {
        update_digits(i*number, digits);
        if(digits.size() == 10) {
            return i*number;
        }
    }
    return -1;
}

int main() {
    int T;
    long long N;
    cin >> T;
    for(int i = 1 ; i <= T ; i++) {
        cin >> N;
        long long result = compute(N);
        cout << "Case #" << i << ": ";
        if(result == -1)
            cout << "INSOMNIA";
        else
            cout << result;
        cout << "\n";
    }
    return 0;
}
