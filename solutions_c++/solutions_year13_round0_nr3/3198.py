#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool bit(int64 mask, int k) {
    return ((1LL << k) & mask) != 0;
}

int64 twice(int64 n, bool repeat_first) {
    int64 k = n;
    bool repeat = repeat_first;
    while (k > 0) {
        if (repeat) {
            int d = k % 10;
            n *= 10;
            n += d;
        }
        k /= 10;
        repeat = true;
    }
    return n;
}

vi digits;
bool is_palindrome(int64 n) {
    digits.clear();
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    for (int i = 0, j = digits.size() - 1; i < j; ++i, --j) {
        if (digits[i] != digits[j])
            return false;
    }
    return true;
}

const int64 MAX = 100000000000000LL;
int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    vector<int64> the_numbers;
    for (int64 n = 1; ; ++n) {
        int64 k = twice(n, false);
        if (k > MAX / k) {
            break;
        }
        if (is_palindrome(k * k))
            the_numbers.push_back(k * k);
        k = twice(n, true);
        if (k <= MAX / k) {
            if (is_palindrome(k * k))
                the_numbers.push_back(k * k);
        }
    }
    sort(the_numbers.begin(), the_numbers.end());
    cerr << "There are " << the_numbers.size() << " such numbers." << endl;
    for (int i = 0; i < the_numbers.size(); ++i) {
        cerr << the_numbers[i] << endl;
    }

    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        int a, b;
        cin >> a >> b;
        int res = 0;
        for (int i = 0; i < the_numbers.size(); ++i) {
            int n = the_numbers[i];
            if (n >= a && n <= b)
                ++res;
        }
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}