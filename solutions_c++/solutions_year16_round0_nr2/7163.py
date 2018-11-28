#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;



void removeCharsFromString( string &str, const char* charsToRemove ) {
    for ( unsigned int i = 0; i < strlen(charsToRemove); ++i ) {
        str.erase( remove(str.begin(), str.end(), charsToRemove[i]), str.end() );
    }
}

int solve(string n){
    int sum = 0;
    char last = n[0];
    for(string::size_type i = 1; i < n.size(); ++i) {
        if (last == n[i]){
            continue;
        }
        if (last == '+' && n[i] == '-'){
            sum += 1;
        }
        if (last == '-' && n[i] == '+'){
            sum += 1;
        }
        last = n[i];
    }
    if (last == '-'){
        sum += 1;
    }
    return sum;
}


int main() {
    int t;
    string n;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << endl;
    }

}
