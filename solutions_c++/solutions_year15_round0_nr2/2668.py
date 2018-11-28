#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> V;
vector<int> V2;

int run_once(int C) {
    int mx = 0;
    for (int i=0; i<(int)V.size(); i++) {
        mx = max(mx, V[i]);
    }
    int mn = mx;

    for (int target=1; target<mx; target++) {
        int res = 0;
        for (int i=0; i<(int)V.size(); i++) {
            int mult = V[i] / target + ((V[i] % target) ? 1 : 0);
            res += mult - 1;
            V2[i] = V[i] / mult + ((V[i] % mult) ? 1 : 0);
        }
        int lmx = 0;
        for (int i=0; i<(int)V.size(); i++) {
            lmx = max(lmx, V2[i]);
        }
        res += lmx;
        mn = min(mn, res);
    }
    return mn;
}

int main() {
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int N; fin >> N;
    int C; string S;
    for (int i=0; i<N; i++) {
        fin >> C;
        V.clear(); V2.clear();
        for (int j=0; j<C; j++) {int t; fin >> t; V.push_back(t); V2.push_back(t);}
        fout << "Case #" << i+1 << ": " << run_once(C);
        fout << endl;
    }
    return 0;
}
