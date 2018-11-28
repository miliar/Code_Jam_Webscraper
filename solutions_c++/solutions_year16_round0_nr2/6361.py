#include <iostream>
#include <ctime>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <string>
#define ll long long 

#define FOR(i,a,b) for(ll i=(a);i<(b);i++)
#define IFOR(i,a,b) for(int i=(b-1);i>(a-1);i--)

using namespace std;

int T;

int parse(string str, int pos, bool reverse){
    int val = 0;
    while(pos >= 0) {
        if (!reverse && str[pos] == '-' || reverse && str[pos] == '+') {
            reverse = !reverse;
            val++;
        }
        pos--;
    }
    return val;
}

int main() {
    clock_t start = clock();
    ofstream out;
    out.open("sol");
    ifstream fileIn;
    fileIn.open("out.out");
    
    cin >> T;
    
    string str;
    FOR(i,0,T) {
        cin >> str;
        out << "Case #" << i+1 << ": " << parse(str, str.length(), false) << endl;
    }
    
    out.close();
    fileIn.close();

    cout << "Timing: " << ( clock() - start ) / (double) CLOCKS_PER_SEC << endl;
    return 0;
}
