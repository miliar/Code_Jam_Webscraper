#include <iostream>
#include <string>
#include <fstream>
using namespace std;


ifstream fin("A-small-attempt0.in");
ofstream fout("a.out");
long long rad , t;
int main() {
    int T , k = 1;
    fin >> T;
    while(T--) {
        fin >> rad >> t;
        long long l = 1 , r = 1000000000;
        while(l < r) {
            long long n = (l+r)/2+1;
            long long tmp = n*n*2+n*(2*rad-1);
            //cout << l << ' ' << r << ' ' << n << ' ' << tmp<< endl;
            if(tmp > t) r = n-1;
            else l = n;
        }
        fout << "Case #" << k++ << ": " << l << endl;
    }
    return 0;
}
