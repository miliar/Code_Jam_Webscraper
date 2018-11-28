#include <cstdio>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <list>
using namespace std;

int counter = 0;
ifstream inFile("C:/tmp/file.in");
ofstream outFile("C:/tmp/file.out");
void make() {

    int n = 0,a,b,k;
    inFile >> a;
    inFile >> b;
    inFile >> k;
    --k;
    for(int i = 0; i < a; i++) {
        for(int j = 0; j < b; j++) {
          if((i&j) <= k)
              n++;
        }
    }


    outFile  << "Case #" << ++counter << ": " << n << endl;

}

int main() {

    int t; inFile >> t;
    inFile.ignore();
    while(t--) {
        make();
    }
    return 0;
}
