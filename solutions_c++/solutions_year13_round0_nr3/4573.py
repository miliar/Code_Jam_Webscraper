#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

int pendro(int p) {
    int x = p;
    int r = 0;
    int q = 0;
    while (x) {
        r = x % 10;
        x /= 10;
        q = q * 10 + r;
    }
    return q;
}

int main(int argc, char** argv) {

    ifstream in("input.in");
    ofstream out("output.out");

    int N, A, B;
    string str;

    in >> N;
    getline(in, str);
    for (int cs = 0; cs < N; cs++) {
        in >> A >> B;
        getline(in, str);
        int a = ceil(sqrt(A));
        int b = floor(sqrt(B));
        int pc=0;
        for (int i = a; i <= b; i++) {
            int p;
            int sq;
            int psq;
            p = pendro(i);

            if (p == i) {
                sq = pow(p, 2);
                psq =  pendro(sq);

                if (sq == psq) {
                    pc++;
                }
            }
        }
        out << "Case #" << cs+1 <<": " << pc << endl;
    }
    return 0;
}

