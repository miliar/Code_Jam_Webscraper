#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
#include <string>
using namespace std;

int run_once(int C, string S) {
    int cnt = 0;
    int res = 0;
    for (int i=0; i<=C; i++) {
        int local = S[i] - '0';
        for (int j=0; j<local; j++) {
            if (cnt < i) {
                res += i-cnt;
                cnt = i;
            }
            cnt++;
        }
    }
    return res;
}

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int N; fin >> N;
    int C; string S;
    for (int i=0; i<N; i++) {
        fin >> C >> S;
        fout << "Case #" << i+1 << ": " << run_once(C, S);
        fout << endl;
    }
    return 0;
}
