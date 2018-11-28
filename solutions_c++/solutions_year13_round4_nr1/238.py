#include <iostream>
#include <fstream>
using namespace std;

#define FNAME "test"
ifstream in(FNAME ".in");
ofstream out(FNAME ".out");

#define PRINT(E) out << E; cout << E

void do_case(int cn) {
    PRINT("Case #" << cn << ": Hello, World!" << endl);
}

int main() {
    int T;
    in >> T;
    for(int it=1;it<=T;it++) do_case(it);
    out.close();
    return 0;
}

