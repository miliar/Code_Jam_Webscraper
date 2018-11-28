#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <fstream>

using namespace std;


vector < int > nums(long long a) {
    vector < int > x (10, 0);
    while (a > 0) {
        x[a % 10] = 1;
        a /= 10;
    }
    return x;
}


int main() {
    fstream cin("/Users/Roman/Desktop/GCJ/input.txt");
    fstream cout("/Users/Roman/Desktop/GCJ/output.txt");
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(18);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        long long n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << tt + 1 << ": INSOMNIA\n";
            continue;
        }
        int num = 0;
        long long temp = 0;
        vector < int > x(10, 1);
        while (num != 10) {
            temp += n;
            auto ans = nums(temp);
            for (int i = 0; i < ans.size(); ++i) {
                if (ans[i] == 1) {
                    num += x[i];
                    x[i] = 0;
                }
            }
        }
        cout << "Case #" << tt + 1 << ": " << temp << "\n";
    }
    return 0;
}