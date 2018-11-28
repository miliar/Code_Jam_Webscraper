#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <bitset>

using namespace std;

long long to_base(string s, int base) {
    long long res = 0;
    for (int i = 0; i < s.size(); ++i) {
        res *= base;
        res += (s[i] == '1');
    }
    return res;
}

int is_prime(long long n) {
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return i;
        }
    }
    return 0;
}

bool is_jamcoins(string n) {
    if (!(n[0] == n.back() && n[0] == '1')) {
        return false;
    }
    for (int i = 2; i <= 10; ++i) {
        if (is_prime(to_base(n, i)) == 0) {
            return false;
        }
    }
    return true;
}


int main() {
//    const int t = 16;
//    for (int q = t; q <= t; ++q) {
//        ofstream cout(to_string(q) + ".txt");
//        vector <string> res;
//        for (int i = 1<<(q-1); i < 1 << q && res.size() < 50; ++i) {
//            string s = bitset<t> (i).to_string();
//            if (is_jamcoins(s)) {
//                res.push_back(s);
//            }
//        }
//        cout << res.size() << "\n";
//        for (int i = 0; i < res.size(); ++i) {
//            cout << res[i] << "\n";
//        }
//    }
    
// Small dataset:
    ifstream cin("16.txt");
    ofstream cout("C-small.out.txt");
    cout << "Case #1:\n";
    int t;
    cin >> t;
    for (int i = 0; i < 50; ++i) {
        string s;
        cin >> s;
        cout << s << " ";
        for (int j = 2; j <= 10; ++j) {
            cout << is_prime(to_base(s, j)) << " ";
        }
        cout << "\n";
    }
    
    
//        cout <<  "Case #" << q << ": " << len - (last == '+') << "\n";
}
