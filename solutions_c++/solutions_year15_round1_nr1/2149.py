#include <fstream>
using namespace std;

int T; // T <= 100
int N;  // 2 <= N <= 1000
int v[1001];

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> T;
    int casenum = 1;
    while (T--) {
        fin >> N;
        for (int i = 0; i < N; i++) {
            fin >> v[i];
        }

        int res1 = 0, res2 = 0;
        // cal res1
        for (int i = 1; i < N; i++) {
            if (v[i] < v[i - 1]) {
                // eat
                res1 += v[i - 1] - v[i];
            }
        }
        // cal res2
        int rate = 0;
        for (int i = 1; i < N; i++) {
            if (v[i] < v[i - 1]) {
                if (v[i - 1] - v[i] > rate) {
                    rate = v[i - 1] - v[i];
                }
            }
        }
        for (int i = 0; i <= N - 2; i++) {
            if (v[i] > rate) {
                res2 += rate;
            } else {
                res2 += v[i];
            }
        }
        // print
        fout << "Case #" << casenum << ": " << res1 << " " << res2 << endl;
        casenum++;
    }
    return 0;
}