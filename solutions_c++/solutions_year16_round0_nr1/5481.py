using namespace std;

#include <iostream>
#include <fstream>

void init(bool* vect) {
    for (int i=0; i<10; i++) {
        vect[i] = false;
    }
}

void analyzeN(int N, bool* vect) {
    if (N == 0) {
        vect[0] = true;
        return;
    }

    while (N != 0) {
        vect[N%10] = true;
        N = N / 10;
    }
    return;
}

bool allTrue(bool* vect) {
    for (int i=0; i<10; i++) {
        if (!vect[i]) {
            return false;
        }
    }
    return true;
}

int main(int argc, char* argv[]) {

    fstream in;
    in.open(argv[1], fstream::in);
    fstream out;
    out.open("output.txt", fstream::out);
    int nTests;
    in >> nTests;

    for (int i=0; i<nTests; i++) {
        int startN, N, prevN;
        in >> startN;
        N = startN;
        bool vect[10];
        init(vect); //init to false
        int counter = 2;
        int breakCode = 0;

        while (1) {
           analyzeN(N, vect);
           prevN = N;
           N = counter * startN;
           if (N == prevN) {
               breakCode = 1;
               break;
           }

           counter++;
           if (allTrue(vect)){
               breakCode = 2;
               break;
           }
        }

        out << "Case #" << i+1 << ": ";
        if (breakCode == 2) {
            out << prevN << endl;
        } else {
            out << "INSOMNIA" << endl;
        }
    }

    return 0;
}
