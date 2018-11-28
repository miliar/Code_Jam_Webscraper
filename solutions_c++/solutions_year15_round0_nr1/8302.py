#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <queue>

#define UREP(i,n) for(unsigned int i=0;i<n;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOREVER for(;;)

typedef unsigned long long int ULINT;
typedef long long int LINT;

using namespace std;

void process(int t) {
    int inv = 0, s = 0;
    int smax;
    cin >> smax;
    string d;
    cin.ignore();
    getline(cin, d);
    // cout << '\'' << d << '\'' << endl;
    for(int i = 0; i <= smax; ++i) {
        int si = d[i] - '0';
        // cout << "ST " << s << " I " << i << " SI " << si << endl;
        if(s < i) {
            inv += i - s;
            s += i - s;
        }
        s += si;
    }


    cout << "Case #" << t << ": " << inv << endl;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    REP(i, t)
        process(i+1);

    return 0;
}
