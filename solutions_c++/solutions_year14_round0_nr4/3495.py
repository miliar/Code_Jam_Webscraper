#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int t, n;
double Neomi[1000], Ken[1000];

int main() {
    ifstream fin("D.in");
    ofstream fout("D.out");
    fin >> t;
    for (int t1 = 0; t1 < t; t1++) {
        fin >> n;
        for (int i = 0; i < n; i++) {
            fin >> Neomi[i];
        }
        for (int i = 0; i < n; i++) {
            fin >> Ken[i];
        }
        sort(Neomi, Neomi + n);
        sort(Ken, Ken + n);

        /// DECEIT WAR
        int nscore = 0;
        for (int i = n - 1, j = n - 1; i >= 0 && j >= 0; j--) {
            if (Neomi[i] > Ken[j]) {
                nscore++;
                i--;
            }
        }
        fout << "Case #" << t1 + 1 << ": " << nscore << " ";

        /// NORMAL WAR
        nscore = n;
        for (int i = n - 1, j = n - 1; i >= 0 && j >= 0; j--) {
            if (Ken[i] > Neomi[j]) {
                nscore--;
                i--;
            }
        }
        fout << nscore << endl;
    }
}
