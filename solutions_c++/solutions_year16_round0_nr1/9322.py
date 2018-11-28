#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

void getDigits(int n, vector<int>& digits) {
    while(n) {
        int digit = n % 10;
        n /= 10;
        digits[digit]++;
    }
}

int solution(int n) {
    vector<int> digits(10, 0);
    unordered_set<int> dict;
    for (int i = 1; i < 10E6; ++i) {
        int num = i * n;
        if (dict.find(num) != dict.end()) {
            return -1;
        }
        dict.insert(num);
        getDigits(num, digits);
        bool found = true;
        for (int j = 0; j < 10; ++j) {
            if (!digits[j]) {
                found = false;
                break;
            }
        }
        if (found) {
            return num;
        }
    }
    return -1;
}

int main() {
    int t, n;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n and then m.
        int result = solution(n);
        if (result == -1) {
            cout << "Case #" << i << ": " <<  "INSOMNIA" << endl;
        } else {
            cout << "Case #" << i << ": " <<  result << endl;
        }
    }
    return 0;
}
