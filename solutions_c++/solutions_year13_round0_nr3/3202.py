#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

template<class T>
string to_string(T i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

bool check_palindrom(string str) {
    if (str.length() == 1) return true;
    for (int i = str.length()/2 - 1, j = (str.length() + 1)/2; 
            i >= 0 && j < str.length(); --i, ++j ) {
        if (str[i] != str[j]) {
            return false;
        }
        return true;
    }
}

void solve() {
    long long A, B;
    cin >> A >> B;
    long long counter = 0;
    for (long long a = 0; a*a <= B; ++a) {
        long long N = a*a;
        if (N >= A && check_palindrom(to_string(a)) 
                && check_palindrom(to_string(N))) {
            counter++;
        }
    }
    cout << counter;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
}
