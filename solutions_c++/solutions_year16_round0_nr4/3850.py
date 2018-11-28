#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

long long recurse(int place, int complex, int K, bool last) {
    if(last && place == K)
        return 0;
    if(complex == 1)
        return 0;
    long long ret = 0;
    long long p = (long long)pow((double)K, (double)complex - 2);
    ret += (p*place);
    if (!last || (last && place < K - 1))
        ret += recurse(++place, --complex, K, last);
    if (last && place == K - 1)
        ret += recurse(place, --complex, K, last);
    return ret;
}

int main() {
	ifstream fin("D-small.in");
	ofstream fout("D-small.txt");
    int T;
    fin >> T;
    for (int step = 1; step <= T; step++) {
        int K, C, S; // (Length of original sequence, Complexity, Number Tries)
        fin >> K >> C >> S;
        long long pos[1000];
        for(int i = 0; i < 1000; i++) {
            pos [i] = 0;
        }
        if (C == 1 && S < K) {
            fout << "Case #" << step << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        if (S < (K+(C-1))/C && C!= 1) {
            fout << "Case #" << step << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        if (C == 1)
            for (int i = 0; i < K; i++)
                pos[i] = i+1;
        else if(K == 1)
            pos[0] = 1;

        else {
            int at = 0;
            int check = 0;
            long long step = (long long)pow((double) K, (double)C-1);
            for(int cd = 1; cd <= K;) {
                long long ps = 1 + (check*step);
                if(K-cd+1 < C && K > C) {
                    pos[at] = ps + recurse(cd, C, K, true);
                    cd = K+1;
                }
                else if(K < C) {
                    pos[at] = ps + recurse(cd, K, K, false);
                    cd = K + 1;
                }
                else {
                    pos[at] = ps + recurse(cd, C, K, false);
                    at++; check += C; cd += C;
                }
            }
        }
        fout <<"Case #" << step << ": ";
        for(int i = 0; pos[i] != 0; i++)
            fout << pos[i] << " ";
        fout<< endl;
    }
    return 0;
}
