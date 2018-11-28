#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int run_once(ifstream &fin) {
    int N; int X; fin >> N >> X;
    vector <int> V;
    vector <int> VV;
    for (int i=0; i<N; i++) {
        int t; fin >> t; V.push_back(t);
        VV.push_back(1);
    }
    sort(V.begin(), V.end());
    reverse(V.begin(), V.end());

    int res = 0;
    for (int i=0; i<N; i++) {
        if (VV[i]) {
            res++; int t = X - V[i];
            for (int j=i+1; j<N; j++) {
                if (VV[j] && V[j] <= t) {
                    VV[j] = 0;
                    break;
                }
            }
        }
    }
    return res;

}

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int N;
    fin >> N;
    for (int i=0; i<N; i++) {
        fout << "Case #" << i+1 << ": ";
        fout << run_once(fin);
        fout << endl;
    }
    return 0;
}
