#include <fstream>
#include <cmath>
using namespace std;

int T;
int D;
int p[7];

int ret;

int my_max(int a, int b) {
    return (a > b) ? a : b;
}

int my_ceil(int a, int b) {
    if (a % b == 0) {
        return a / b;
    } else {
        return a / b + 1;
    }
}

void gao(int k, int tmp_max, int plus) {
    if (k == D + 1) {
        if (ret == -1 || tmp_max + plus < ret) {
            // update
            ret = tmp_max + plus;
        }
        return;
    }

    for (int i = 1; i <= p[k]; i++) {
        gao(k + 1, my_max(tmp_max, my_ceil(p[k], i)), plus + i - 1);
    }
}

int main() {
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");
    fin >> T;
    int casenum = 1;
    while (T--) {
        fin >> D;
        for (int i = 1; i <= D; i++) {
            fin >> p[i];
        }
        // deal with p[1], .., p[d]
        // init
        ret = -1;
        gao(1, 0, 0);
        fout << "Case #" << casenum << ": " << ret << endl;

        casenum++;
    }
    return 0;
}
