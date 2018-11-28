
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <fcntl.h>
#include <unistd.h>
#include <fstream>

using namespace std;

typedef long long INT;
typedef vector<INT> INTVec;
typedef vector<INTVec> Mat;



int main(int argc, char *argv[]) {
    // ifstream inFile("B.tiny");
    ifstream inFile("B-small-attempt0.in");
    ofstream outFile("B-small-attempt0.out");
    istream &in = inFile;
    ostream &out = outFile;
    // istream &in = cin;
    // ostream &out = cout;
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        int A, B, K;
        in >> A >> B >> K;
        int cnt = 0;
        for (size_t j = 0; j < A; ++j) {
            for (size_t k = 0; k < B; ++k) {
                int res = j & k;
                if (res < K) ++cnt;
            }
        }

        out << "Case #" << i+1 << ": " << cnt << endl;
    }
    return 0;
}

