#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

typedef long int int64;

//void getDivisor(vector<int64>& jamcoins, vector<int64>& divisors) {
//    for (int i = 0; i < 9; ++i) {
//        int64 number = jamcoins[i];
//        for (int64 j = 2; j < sqrt(number) + 1; ++j) {
//            if (number % j == 0) {
//                divisors.push_back(j);
//                break;
//            }
//        }
//    }
//}

//void getJamCoins(int length, int count, unordered_map<string, vector<int64>>& jamcoins) {
//    for (int64 i = 0; i < up; ++i) {
//        int64 number = up + (i << 1) + low;
//        bool prime = true;
//        for (int64 j = 2; j < sqrt(number) + 1; ++j) {
//            if (number % j == 0) {
//                prime = false;
//                break;
//            }
//        }
//        if (!prime) {
//            jamcoins.push_back(number);
//        }
//        if (jamcoins.size() == count) {
//            return;
//        }
//    }
//}

//void caculate(int length, int count) {
//    unordered_map<string, vector<int64>> jamcoins;
//    getJamCoins(length, count, jamcoins);
//    for (int i = 0; i < count; ++i) {
//        vector<int64> divisors(9, 0);
//        getDivisor(jamcoins[i], divisors);
//        cout << jamcoins[i] << " ";
//        for (int j = 0; j < 8; ++j) {
//            cout << divisors[0] << " ";
//        }
//        cout << divisors[9] << endl;
//    }
//}

int flip(int *a, int n) {
    int i1, m, i, j;
    char b;
    for (m = 0; ; m++) {
        if (a[0] == 1) {
            for (i1 = 0; (i1 < n - 1) && (a[i1 + 1] == 1); i1++);
            if (i1 == n - 1)
                break;
        }
        else for (i1 = n - 1; (i1 >= 0) && (a[i1] == 1); i1--, n--);
        for (i = 0, j = i1; i <= j; i++, j--) {
            b = 1 - a[i];
            a[i] = 1 - a[j];
            a[j] = b;
        }
    }
    return m;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        cin >> s;
        vector<int> input;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '-') {
                input.push_back(0);
            } else {
                input.push_back(1);
            }
        }
        cout << "Case #" << i << ": " << flip(&input[0], input.size()) << endl;
    }
    return 0;
}
