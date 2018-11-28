//
//  sheep.cpp
//  
//
//  Created by John Nevard on 4/9/16.
//
//

#include <iostream>
#include <vector>

using namespace std;

long sheep(long n) {
    if (!n) return 0;
    vector<bool> digits(10, false);
    int dl = 10;
    long ln = 0;
    for (int i = 0; dl; ++i) {
        ln += n;
        long t = ln;
        while (t) {
            int d = t % 10;
            t /= 10;
            if (!digits[d]) {
                digits[d] = true;
                --dl;
            }
        }
    }
    return ln;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n;
        cin >> n;
        long ln = sheep(n);
        cout << "Case #" << i << ": ";
        if (n)
            cout << ln << '\n';
        else
            cout << "INSOMNIA\n";
    }
    return 0;
}