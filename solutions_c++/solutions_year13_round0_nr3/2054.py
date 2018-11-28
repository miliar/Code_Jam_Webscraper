#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define MX 10000001LL

bool isPalindrome(long long n) {
    stringstream A;
    string s;
    A << n;
    A >> s;
    for (int i = 0; i < s.size() / 2; ++i) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<long long> fair;
    for (long long i = 1; i < MX; ++i) {
        if (isPalindrome(i) && isPalindrome(i * i)) {
            fair.push_back(i * i);
//            cout << i << endl;
        }
    }
    int T;
    cin >> T;
    for (int ind = 1; ind <= T; ++ind) {
        long long A, B;
        cin >> A >> B;
        int ans = 0;
        for (int i = 0; i < fair.size(); ++i) {
            if (fair[i] >= A && fair[i] <= B) {
                ++ans;
            }
        }
        cout << "Case #" << ind << ": " << ans << endl;
    }
}
