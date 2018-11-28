#include <algorithm>

#include <deque>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#include <iostream>

using namespace std;


set<uint64_t> palindromes;
set<uint64_t> fas;

int readInt() {
    string str;
    getline(cin, str);
    int i = stoi(str);
    return i;
}

template <typename T>
bool isPalindrome(T n) {
    string str = to_string(n);
    string str2 = str;
    reverse(str2.begin(), str2.end());
    return (str == str2);
}

void gen() {
    const uint64_t MAX = 20000000;
    for (uint64_t i = 1; i <= MAX; ++i) {
        if (isPalindrome(i)) {
            palindromes.insert(i);
        }
    }

    for (uint64_t p : palindromes) {
        if (isPalindrome(p * p)) {
            fas.insert(p * p);
        }
    }
}

int main(int argc, char* argv[]) {
    gen();

    int numTests = readInt();
    for (int test = 1; test <= numTests; ++test) {
        uint64_t A, B;
        cin >> A >> B;

        set<uint64_t>::const_iterator itA = fas.lower_bound(A), itB = fas.upper_bound(B);
        uint64_t ans = distance(itA, itB);
        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}
