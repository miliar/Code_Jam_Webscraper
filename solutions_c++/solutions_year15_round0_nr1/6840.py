#include <iostream>
#include <fstream>

using namespace std;

int nT;

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

void solve(int tCaseN, int sMax, string shyness) {
    int n = 0;
    int s[shyness.size()];
    for (int i = 0; i < shyness.size(); i++) {
        s[i] = (int)shyness[i] - 48;
    }
    int cS = s[0];
    for (int i = 1; i <= sMax; i++) {
        int added = 0;
        if (cS < i && s[i] != 0) {
            added = i - cS;
            n += added;
        }

        cS += (s[i] + added);
    }

    fout << "Case #" << tCaseN + 1 << ": " << n << endl;
}

int main() {
    fin >> nT;

    for (int i = 0; i < nT; i++) {
        int sMax = 0;
        string shyness;
        fin >> sMax >> shyness;
        solve(i, sMax, shyness);
    }
    fin.close();
    fout.close();
    return 0;
}