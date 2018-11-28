#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
#include <string>
#include <vector>
using namespace std;

void run_once(ifstream& fin, ofstream& fout) {
    vector <int> V;
    int N; fin >> N;
    for (int i=0; i<N; i++) {
        int t; fin >> t;
        V.push_back(t);
    }
    int max = 0; int sum = 0;
    for (int i=0; i<N-1; i++) {
        int diff = V[i] - V[i+1];
        if (diff > max) max = diff;
        if (diff > 0) sum += diff;
    }
    int sum2 = 0;
    for (int i=0; i<N-1; i++) sum2 += V[i] > max ? max : V[i];
    fout << sum << " " << sum2;
}

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int N; fin >> N;
    for (int i=0; i<N; i++) {
        fout << "Case #" << i+1 << ": ";
        run_once(fin, fout);
        fout << endl;
    }
    return 0;
}
