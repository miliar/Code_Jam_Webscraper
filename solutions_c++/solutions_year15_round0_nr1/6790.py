#include <iostream>
#include <fstream>
#include <sstream> 
#include <string>
using namespace std;

int main () {
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-small-attempt3.out", "w", stdout);
    string in_str;
    istringstream iss;
    
    int T, SM, r, s;
    string SS;
    char map[51][51];
    bool possible;
    
    getline (cin, in_str);
    iss.str(in_str);
    iss.clear();
    iss >> T;
    for (int t_c=1; t_c<=T; t_c++ ) {
        getline (cin, in_str);
        iss.str(in_str);
        iss.clear();
        iss >> SM >> SS;
        
        r = 0;
        s = 0;
        for(int i=0; i<=SM; i++) {
            if (s < i && SS[i] != '0') { r += i - s; s = i; }
            s += (int)(SS[i] - '0');
        }
        cout << "Case #" << t_c << ": " << r << endl;
    }
    
    return 0;
}