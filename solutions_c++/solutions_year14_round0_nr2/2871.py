#include <cstdio>
#include <fstream>
#include <iomanip>
using namespace std;



int counter = 0;
ifstream inFile("C:/tmp/file.in");
ofstream outFile("C:/tmp/file.out");
void make() {

    long double a = 2,c,f,x,r1,r2,b =0;

    inFile >> fixed >> setprecision(7) >> c;
    inFile >> fixed >> setprecision(7) >> f;
    inFile >> fixed >> setprecision(7) >> x;
    inFile.ignore();

    r1 = (long double) x/a;
    while(true) {
        b += c/a;
        a += f;
        r2 = b + (long double) x/a;
        if(r2 < r1)
            r1 = r2;
        else
            break;
    }

    outFile  << "Case #" << ++counter << ": " << fixed << setprecision(7) << r1 << endl;
    return;
}

int main() {

    int t; inFile >> t;
    inFile.ignore();
    while(t--) {
        make();
    }
    return 0;
}
