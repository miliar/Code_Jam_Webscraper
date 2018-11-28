#include <assert.h>
#include <string.h>
#include <stack>
#include <queue>
#include <set>
#include <string>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
using namespace std;

#define tint long long int
#define utint long long unsigned int
#define MAXN 1000010
#define DEBUG 0

struct pto {
    int x, y;
    pto() { x = 0; y = 0; }
    pto(int _x, int _y): x(_x), y(_y){};
};

// next_permutation
struct lex_compare {
    bool operator() (const int a, const int b) const{
        return a > b;
    }
};
// sort
bool mycmp(int a, int b) {
    return a > b;
}

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main()
{
    int T = 1;
    cin >> T;
    for (int tt = 0; tt < T; tt++) {
        string s;
        cin >> s;
        int flip = 0;
        int len = s.size();
        for (int i = 1; i < len; i++) {
            if (s[i-1] != s[i]) flip++;
        }
        if (s[len-1] != '+') flip++;
        cout << "Case #" << tt+1 << ": " << flip << endl;
    }
    return 0;
}