#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;



void removeCharsFromString( string &str, const char* charsToRemove ) {
    for ( unsigned int i = 0; i < strlen(charsToRemove); ++i ) {
        str.erase( remove(str.begin(), str.end(), charsToRemove[i]), str.end() );
    }
}

string solve(int n){
    if (n == 0){
        return "INSOMNIA";
    }
    string all = "1234567890";
    for (int i=1;;i++){
        int tmp = n*i;
        removeCharsFromString(all, to_string(tmp).c_str());
        if (all.empty()){
            return to_string(tmp);
        }
    }
    return "";
}


int main() {
    int t,n;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << endl;
    }

}
