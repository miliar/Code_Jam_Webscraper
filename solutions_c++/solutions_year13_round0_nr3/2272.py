#include <iostream>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

bool ispalin(unsigned long long num) {
    stringstream str;
    str << num;
    string tocheck = str.str();
    for (int i = 0, j = tocheck.length() - 1; i < tocheck.length() && j >= 0; i++, j--) {
        if (tocheck[i] != tocheck[j]) {
            return false;
        }
    }
    return true;
}

vector<unsigned long long> belowlarge;

unsigned long long squares(unsigned long long A, unsigned long long B) {
    vector<unsigned long long>::iterator start = lower_bound(belowlarge.begin(), belowlarge.end(), A);
    vector<unsigned long long>::iterator end = upper_bound(belowlarge.begin(), belowlarge.end(), B);
    return distance(start, end);
}

void calcsquares() {
    unsigned long long A = 1;
    unsigned long long B = pow(10, 14);
    unsigned long long lower = sqrt(1) - 1;
    unsigned long long upper = sqrt(pow(10, 14)) + 1;
    for (unsigned long long a = lower; a < upper; a++) {
        if (ispalin(a) && ispalin(a * a) && a * a >= A && a * a <= B) {
            belowlarge.push_back(a * a);
        }
    }
}

int main() {
    calcsquares();
    int T;
    cin >> T;
    for (int g = 1; g <= T; g++) {
        unsigned long long A, B;
        cin >> A >> B;
        cout << "Case #" << g << ": " << squares(A,B) << "\n";
    }
    return 0;
}
