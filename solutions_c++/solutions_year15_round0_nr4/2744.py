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

    int x,r,c;
    cin >> x >> r >> c;

    bool gabrielwins=false;

    switch(x){
        case 1: {
            gabrielwins = true;
            break;
        }
        case 2: {
            if(r%2==0 || c%2==0) gabrielwins = true;
            break;
        }
        case 3: {
            if((r%3==0 || c%3==0) && min(r,c) >=2) gabrielwins = true;
            break;
        }
        case 4: {
            if((r%4==0 || c%4==0) && min(r,c) >=3) gabrielwins = true;
            break;
        }
    }


    cout << "Case #" << caseNum << ": " << (gabrielwins?"GABRIEL":"RICHARD") << endl;
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
