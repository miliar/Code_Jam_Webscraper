#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <climits>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct Mypair {
    Mypair() : p('A'), n(0){}
    Mypair(char _p, int _n) : p(_p), n(_n){}
    char p;
    int n;
};

bool func (Mypair &lhs, Mypair &rhs){
    return lhs.n > rhs.n;
}

int main(){
    ifstream fin("in1");
    ofstream fout("out1");
    int T;

    fin >> T;
    for (int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";

        int N;
        fin >> N;
        vector<Mypair> P(N, Mypair());
        for (int n = 0; n < N; n++){
            P[n].p = 'A' + n;
            fin >> P[n].n;
        }
        sort(P.begin(), P.end(), func);

        while (P[0].n > P[1].n){
            int n = min(2, P[0].n - P[1].n);
            for (int i = 0; i < n; i++)
                fout << P[0].p;
            fout << " ";
            P[0].n -= n;
        }
        for (int i = N - 1; i > 1; i--){
            while (P[i].n > 0){
                int n = min(2, P[i].n);
                for (int j = 0; j < n; j++)
                    fout << P[i].p;
                fout << " ";
                P[i].n -= n;
            }
        }
        for (int i = 0; i < P[0].n; i++)
            fout << P[0].p << P[1].p << " ";
        fout << endl;
    }

    fin.close();
    fout.close();
}
