#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <math.h>
using namespace std;

//#define PI 3.14159

long double area(long double r) {
    return r * r;
}

int main() {
    
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    long int T, c = 1, r, t;
    fin >> T;
    while(T--) {
        int i = 2;
        long int ans = 0;
        fin >> r >> t;
        ans += (area(r + 1) - area(r));
        
        while (ans < t) {
            ans += (area(r + i + 1) - area(r + i));
            if(ans > t)
                break;
            i += 2;
        }
        
        fout <<"Case #" << c << ": " << (int)ceil((long double)i / 2.0) << endl;
        c++;
    }
    return 0;
}