#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int t, l, x;
string s;

int mul[5][5] = {0,0,0,0,0,
                0,1,2,3,4,
                0,2,-1,4,-3,
                0,3,-4,-1,2,
                0,4,3,-2,-1};

int main(){
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");
    in >> t;
    for (int i = 0 ; i < t ; ++i) {
        bool ok(false), ok1(false), ok2(false), ok3(false);
        in >> l >> x >> s;
        if (x > 4) {
            x = x % 4 + 4;
        }
        int result = 1;
        for (int j = 0 ; j < x ; ++j) {
            for (int m = 0 ; m < s.length() ; ++m) {
                if (result < 0) {
                    result = -mul[-result][s[m] - 'g'];
                } else {
                    result = mul[result][s[m] - 'g'];
                }
                if (!ok1) {
                    if (result == 2) {
                        ok1 = true;
                        result = 1;
                    }
                }
                if (ok1 && !ok2) {
                    if (result == 3) {
                        ok2 = true;
                        result = 1;
                    }
                }
            }
        }
        if (ok2 && !ok3 && result == 4){
            ok3 = true;
        }
        ok = ok1 & ok2 & ok3;
        out << "Case #" << i + 1 << ": " << (ok ? "YES" : "NO") << endl;
    }
    in.close();
    out.close();
}