#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cmath>

#define FOR(i, a, b) for(int i = a; i < b; i++)

using namespace std;

int T, K, C, S;

int main()
{
    ifstream fin;
    fin.open("D-small-attempt0.in");
    ofstream fout;
    fout.open("result-small.txt");
    fin >> T;
    FOR(i, 0, T) {
        fin >> K >> C >> S;
        fout << "Case #" << i + 1 << ": ";
        if (S < K/C) {
            fout << "IMPOSSIBLE";
        }
        else {
            FOR(j, 0, ceil((double)(K)/C)) {
                long long pos = 0;
                long long multK = 1;
                FOR(k, 1, C + 1) {
                    pos += (min((C*j + k), K) - 1) * multK;
                    multK = multK * K;
                }
                fout << pos + 1 << ' ';
            }
        }
        fout << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
