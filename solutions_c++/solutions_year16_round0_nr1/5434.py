#include <bits/stdc++.h>
using namespace std;

void treat_digits(int n, unordered_set<int>& digits) {
    while(n) {
        int digit = n % 10;
        if(digits.find(digit) != digits.end()) {
            digits.erase(digit);
        }
        n /= 10;
    }
}

int main() {
    int T;
    cin >>T;
    
    for(int i = 1; i <= T; ++i) {
        int N;
        cin >> N;
        string output = "Case #" + to_string(i) + ": ";
        if(N == 0) {
            output += "INSOMNIA";  
        }
        else {
            unordered_set<int> digits {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            int num = 0;
            while(!digits.empty()) {
                 num += N;
                 treat_digits(num, digits);
            }
            output += to_string(num);
        }
        cout << output + '\n';
    }
}
