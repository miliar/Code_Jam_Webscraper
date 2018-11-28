#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <functional>
#include <numeric>

using namespace std;

#define vi vector<int>
#define vvi vector<vector<int> >
#define all(e) e.begin(),e.end()
#define pb push_back

unsigned long long sumEvenSquares( unsigned long long x ) {
    return 1;
}

unsigned long long sumOddSquares( unsigned long long x ) {
    return 1;
}

int main(int argc, const char *argv[]) {
    int T;
    cin >> T;
    cin.ignore();
    for(int ca=0; ca<T; ca++) {
        unsigned long long r,t;
        cin >> r >> t;

        // x*x - (x-1)*(x-1)
        // 2*x -1
        // 4*4 - 3*3 = 16 - 9 = 7

        unsigned long long maxRings = 0;

        unsigned long long paint = 0;
        unsigned long long i=r+1;

        // 2*2-1 + 4*2-1

        // UGLY!!
        while(true) {
            unsigned long long painti = 2*i-1;
            paint += painti;
            //std::cout << "paint " << i<< "="<<painti<<endl;
            i += 2;
            if(paint > t) break;
            maxRings++;
        }
        
        cout << "Case #" << (ca+1) << ": " << maxRings << endl;
    }
    return 0;
}

