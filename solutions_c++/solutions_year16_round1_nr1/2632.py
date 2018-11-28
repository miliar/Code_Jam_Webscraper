#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    ifstream fi("in");
    ofstream fw("out");

    int T;

    fi >> T ;
    for(int i=0; i<T ; ++i) {
        string s;
        string fiw;

        fi >> s;
        fiw = "";
        char fc = '\0';

        for(auto l: s) {
            // cout << l << endl;
            if (fc == '\0') {
                fc = l;
                fiw += l;
            } else {
                if(l >= fc) {
                    fiw = l + fiw;
                    fc = l;
                } else {
                    fiw += l;
                }
            }
        }

        cout << fiw << endl;
        fw << "Case #" << (i+1) << ": " << fiw << endl;


    }


    fw.close();
    fi.close();
    return 0;
}