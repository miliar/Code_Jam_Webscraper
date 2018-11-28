#include <iostream>
#include <iomanip>
#include <vector>
#include <limits>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <queue>
#include <set>
#include <bitset>
#include <map>

#define UREP(i,n) for(unsigned int i=0;i<n;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define FRVR for(;;)

typedef unsigned long long int ULINT;
typedef long long int LINT;

const double EPS = 1e-6;

using namespace std;

void process(int caseNum) {
    int s;
    cin >> s;
    int standing = 0, friends = 0;
    REP(i, s+1) {
        char dc;
        cin >> dc;
        int d = dc - '0';
        if(standing<i) {
            friends += i-standing;
            standing = i;
        }
        standing+=d;
    }
    cout << "Case #" << caseNum << ": " << friends << endl;
}

int main() {
    ios_base::sync_with_stdio(false);

    int t, caseNum=1;
    cin >> t;
    REP(i, t) {
        process(caseNum++);
    }

    return 0;
}
