#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;
int i, j, k, k2, n, t, a, b, result;
char temp;
bool check;
int main() {
    ifstream fin;
    ofstream fout;
    fin.open("B-small-attempt0.in");
    fout.open("A-small-practice.out");
    fin >> t;
    for (k2 = 0; k2 < t; ++k2) {
        fin >> a >> b >> k;
        result = 0;
        for (i = 0; i < a; ++i) {
            for (j = 0; j < b; ++j) {
                if ((i&j) < k) result++;
            }
        }

        fout << "Case #" << k2 + 1 << ": " << result << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
