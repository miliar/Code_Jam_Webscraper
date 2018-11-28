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

unsigned int getdigits(utint n)
{
    unsigned int count = 0;
    do {
        count |= (1 << (n%10));
        n /= 10;
    } while (n);
    return count;
}

int main()
{
    int T = 1;
    cin >> T;
    for (int tt = 0; tt < T; tt++) {
        utint n;
        cin >> n;
        const unsigned int ALLDIGITS = 1023;
        unsigned int count = 0;
        int sol = 0;
        while (n && count != ALLDIGITS) {
            sol++;
            utint num = n*sol;
            count |= getdigits(num);
        }
        cout << "Case #" << tt+1 << ": ";
        if (sol == 0) cout << "INSOMNIA" << endl;
        else cout << n*sol << endl;
    }
    return 0;
}